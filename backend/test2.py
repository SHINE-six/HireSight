
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from joblib import load
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from xgboost import XGBClassifier

# Initialize the lemmatizer and stopwords list once to optimize performance
lemmatizer = WordNetLemmatizer()
useless_words = stopwords.words("english")

mbti_mapping = {
    0: 'INFJ', 1: 'ENTP', 2: 'INTP', 3: 'INTJ',
    4: 'ENTJ', 5: 'ENFJ', 6: 'INFP', 7: 'ENFP',
    8: 'ISFP', 9: 'ISTP', 10: 'ISFJ', 11: 'ISTJ',
    12: 'ESTP', 13: 'ESFP', 14: 'ESTJ', 15: 'ESFJ'
}

def translate_prediction_to_mbti(prediction, mapping):
    return mapping[prediction[0]]

def pre_process_sentence(sentence, remove_stop_words=True):
    sentence = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ', sentence)
    sentence = re.sub(r'[^a-zA-Z]+', ' ', sentence).lower()
    sentence = re.sub(r'([a-z])\1{2,}', '', sentence)
    words = sentence.split()
    if remove_stop_words:
        words = [word for word in words if word not in useless_words]
    return ' '.join([lemmatizer.lemmatize(word) for word in words])

def generate_wordcloud(text, mbti_type):
    wordcloud = WordCloud(width = 800, height = 400, background_color ='white', stopwords = set(STOPWORDS)).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title(f"Word Cloud for {mbti_type}")
    plt.show()

def main(text):
    model_xgb = load('model_xgb.joblib')
    vectorizer = load('tfidf_vectorizer.joblib')
    preprocessed_text = pre_process_sentence(text)
    vectorized_text = vectorizer.transform([preprocessed_text])
    predicted_class = model_xgb.predict(vectorized_text)
    predicted_mbti = translate_prediction_to_mbti(predicted_class, mbti_mapping)
    print("Predicted MBTI type:", predicted_mbti)
    generate_wordcloud(preprocessed_text, predicted_mbti)

if __name__ == "__main__":
    text = "I am introvert and I like to read books and play games. I am a software engineer."
    main(text)
