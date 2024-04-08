# Data Analysis
import pandas as pd
import numpy as np
import json
# Data Visualization
import matplotlib.pyplot as plt
import wordcloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image

# Text Processing
import re
from sklearn.preprocessing import LabelEncoder
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Machine Learning packages
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

# Model training and evaluation
from sklearn.model_selection import train_test_split

#Models
from xgboost import XGBClassifier


lemmatiser = WordNetLemmatizer()

useless_words = stopwords.words("english")

unique_type_list = [x.lower() for x in ['INFJ', 'ENTP', 'INTP', 'INTJ', 'ENTJ', 'ENFJ', 'INFP', 'ENFP',
                                       'ISFP', 'ISTP', 'ISFJ', 'ISTJ', 'ESTP', 'ESFP', 'ESTJ', 'ESFJ']]


b_Pers_dict = {'I':0, 'E':1, 'N':0, 'S':1, 'F':0, 'T':1, 'J':0, 'P':1}
b_Pers_list = [{0:'I', 1:'E'}, {0:'N', 1:'S'}, {0:'F', 1:'T'}, {0:'J', 1:'P'}]

def translate_personality(personality):
    return [b_Pers_dict[l] for l in personality]

def translate_back(personality):
    s = ""
    for i, l in enumerate(personality):
        s += b_Pers_list[i][l]
    return s


personality_type = ["IE: Introversion (I) / Extroversion (E)", 
                   "NS: Intuition (N) / Sensing (S)", 
                   "FT: Feeling (F) / Thinking (T)", 
                   "JP: Judging (J) / Perceiving (P)"]


def pre_process_text(data, remove_stop_words=True, remove_mbti_profiles=True):
    list_personality = []
    list_posts = []

    for _, row in data.iterrows():
        posts = row['posts']

        # Remove URL links
        posts = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ', posts)

        # Remove non-words and excess spaces
        posts = re.sub(r'[^a-zA-Z]+', ' ', posts).lower()

        # Remove repeating letters
        posts = re.sub(r'([a-z])\1{2,}', '', posts)

        # Remove stop words
        words = posts.split() if remove_stop_words else posts.split()
        words = [lemmatiser.lemmatize(w) for w in words if w not in useless_words]
        posts = ' '.join(words)

        # Remove MBTI personality words
        if remove_mbti_profiles:
            posts = re.sub(r'\b(?:' + '|'.join(unique_type_list) + r')\b', '', posts)

        # Transform MBTI to binary vector
        type_labelized = translate_personality(row['type'])
        list_personality.append(type_labelized)
        list_posts.append(posts)

    return np.array(list_posts), np.array(list_personality)


def train_xgboost_model(X, Y, param):
    model = XGBClassifier(**param)
    model.fit(X, Y)
    return model


def generate_wordcloud(data, image_path, title):
    mask = np.array(Image.open(image_path))
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(background_color="white", max_words=2000, mask=mask, stopwords=stopwords)
    wordcloud.generate(data)
    image_colors = ImageColorGenerator(mask)

    plt.figure(figsize=(8, 4))
    plt.subplot(121)
    plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    plt.subplot(122)
    plt.imshow(mask, cmap=plt.cm.gray, interpolation="bilinear")
    plt.axis("off")
    plt.suptitle(f"Word Cloud for {title}", fontsize=16)
    plt.tight_layout()

    # Save the image
    plt.savefig("wordcloud.png")
    plt.show()

def save_to_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def save_processed_data(posts, personalities, file_path):
    np.savez(file_path, posts=posts, personalities=personalities)

def load_processed_data(file_path):
    data = np.load(file_path)
    return data['posts'], data['personalities']

def main():
    try:
        list_posts, list_personality = load_processed_data("C:\\Users\\annin\\OneDrive\\Desktop\\HireSight\\processed_data.npz")
    except FileNotFoundError:
        data = pd.read_csv("C:\\Users\\annin\\OneDrive\\Desktop\\HireSight\\backend\\mbti_1.csv")
        list_posts, list_personality = pre_process_text(data, remove_stop_words=True, remove_mbti_profiles=True)
        save_processed_data(list_posts, list_personality, "processed_data.npz")

    # Feature extraction
    cntizer = CountVectorizer(analyzer="word", max_features=1000, max_df=0.7, min_df=0.1) 
    X_cnt = cntizer.fit_transform(list_posts)

    tfizer = TfidfTransformer()
    X_tfidf =  tfizer.fit_transform(X_cnt).toarray()
    X = X_tfidf

    # XGBoost parameters
    param = {'n_estimators': 200, 'max_depth': 2, 'nthread': 8, 'learning_rate': 0.2}

    # Predict personality type 
    mydata = pd.DataFrame(data={'type': [''], 'posts': [posts]})
    my_posts, dummy = pre_process_text(mydata, remove_stop_words=True, remove_mbti_profiles=True)
    my_X_cnt = cntizer.transform(my_posts)
    my_X_tfidf =  tfizer.transform(my_X_cnt).toarray()

    result = []
    for l in range(len(personality_type)):
        Y = list_personality[:,l]
        model = train_xgboost_model(X, Y, param)
        y_pred = model.predict(my_X_tfidf)
        result.append(y_pred[0])

    predicted_personality = translate_back(result)
    print("Predicted personality type for provided transcript:", predicted_personality)

    # Generate word cloud
    my_posts_str = " ".join(my_posts)
    image_path = f'C:\\Users\\annin\\OneDrive\\Desktop\\HireSight\\backend\{predicted_personality.lower()}.jpg'
    generate_wordcloud(my_posts_str, image_path, predicted_personality)

    mbti_data = {
        'type': predicted_personality,
        'image_path': image_path
    }
    save_to_json(mbti_data, 'mbti_data.json')

if __name__ == "__main__":
    posts = "I find comfort in structure and routine."
    main()