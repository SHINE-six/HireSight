import json
import re
from joblib import load
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import warnings
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib
matplotlib.use('Agg')  # Set the backend to 'Agg' for non-GUI backend before importing pyplot
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore", category=UserWarning)

# Load trained components
model = load("C:\\hilti\\HireSight\\backend\\model\\mbti_xgb_personality_model.joblib")
vectorizer = load("C:\\hilti\\HireSight\\backend\\model\\mbti_vectorizer.joblib")
tfizer = load("C:\\hilti\\HireSight\\backend\\model\\mbti_tfidf_transformer.joblib")
label_encoder = load("C:\\hilti\\HireSight\\backend\\model\\mbti_label_encoder.joblib")

# Initialize the lemmatizer and stopwords list
lemmatizer = WordNetLemmatizer()
stopwords_list = stopwords.words("english")

def save_to_json(data, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def clean_text(text):
    """Clean and preprocess the text."""
    # Initialize the lemmatizer and stopwords list
    lemmatizer = WordNetLemmatizer()
    stopwords_list = stopwords.words("english")
    mbti_types = ['infj', 'entp', 'intp', 'intj', 'entj', 'enfj', 'infp', 'enfp',
                  'isfp', 'istp', 'isfj', 'istj', 'estp', 'esfp', 'estj', 'esfj']

    # Clean the text
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    text = re.sub(r'[^a-zA-Z ]', '', text).lower()
    words = text.split()

    # Remove stopwords and MBTI types
    cleaned_words = [lemmatizer.lemmatize(word) for word in words if word not in stopwords_list and word not in mbti_types]
    return ' '.join(cleaned_words)

def generate_wordcloud(data, image_path, title):
    """Generate and save a word cloud image."""
    mask = np.array(Image.open(image_path))
    wordcloud = WordCloud(background_color="white", max_words=2000, mask=mask, stopwords=set(STOPWORDS))
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
    plt.close()  # Close the figure to avoid the warning

def preprocess_and_predict(new_text):
    """Process the text, vectorize it, and predict the personality type."""
    processed_text = clean_text(new_text)
    X_new_cnt = vectorizer.transform([processed_text])
    X_new_tfidf = tfizer.transform(X_new_cnt)
    y_pred_encoded = model.predict(X_new_tfidf)
    return label_encoder.inverse_transform(y_pred_encoded)[0], processed_text

def main(text):
    """Function to be called for making predictions and managing outputs."""
    predicted_personality, processed_text = preprocess_and_predict(text)
    print(f"The predicted personality type is: {predicted_personality}")
    
    # Generate word cloud and save JSON data
    image_path = f'C:\\hilti\\HireSight\\backend\\mbtiFolder\\mbti_pic\\{predicted_personality.lower()}.jpg'
    generate_wordcloud(processed_text, image_path, f"Personality Type - {predicted_personality}")
    
    mbti_data = {
        'type': predicted_personality,
        'image_path': image_path
    }
    save_to_json(mbti_data, 'mbti_data.json')
    
    return predicted_personality


# If the script is run directly, allow the user to input text
if __name__ == "__main__":
    while True:
        text = input("Enter text to predict personality type (type 'exit' to quit): ")
        if text.lower() == 'exit':
            break
        personality = main(text)
