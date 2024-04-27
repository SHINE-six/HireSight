import re
import nltk
from tqdm import tqdm
from Lemmatizer import Lemmatizer
from joblib import load
from nltk.corpus import stopwords

nltk.download('wordnet')

nltk.download('stopwords')


# This mapping should match the one you used when encoding MBTI types into numeric labels
mbti_mapping = {
    0: 'INFJ', 1: 'ENTP', 2: 'INTP', 3: 'INTJ',
    4: 'ENTJ', 5: 'ENFJ', 6: 'INFP', 7: 'ENFP',
    8: 'ISFP', 9: 'ISTP', 10: 'ISFJ', 11: 'ISTJ',
    12: 'ESTP', 13: 'ESFP', 14: 'ESTJ', 15: 'ESFJ'
}

def translate_prediction_to_mbti(prediction, mapping):
    # Assume prediction is a list or an array-like structure with one element
    return mapping[prediction[0]]

# Initialize the lemmatizer and stopwords list once to optimize performance
useless_words = stopwords.words("english")
unique_type_list = [x.lower() for x in ['INFJ', 'ENTP', 'INTP', 'INTJ', 'ENTJ', 'ENFJ', 'INFP', 'ENFP',
                                        'ISFP', 'ISTP', 'ISFJ', 'ISTJ', 'ESTP', 'ESFP', 'ESTJ', 'ESFJ']]

def pre_process_sentence(sentence, remove_stop_words=True, remove_mbti_profiles=True):
    # Remove URL links
    sentence = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ', sentence)
    # Remove non-words and excess spaces
    sentence = re.sub(r'[^a-zA-Z]+', ' ', sentence).lower()
    # Remove repeating letters
    sentence = re.sub(r'([a-z])\1{2,}', '', sentence)
    # Tokenize, remove stop words, and lemmatize
    words = sentence.split()
    if remove_stop_words:
        words = [word for word in words if word not in useless_words]
    words = [Lemmatizer.lemmatize(word) for word in words]
    sentence = ' '.join(words)
    # Remove MBTI personality words if required
    if remove_mbti_profiles:
        sentence = re.sub(r'\b(?:' + '|'.join(unique_type_list) + r')\b', '', sentence)

    return sentence

def clear_text(data):
    data_length=[]
    cleaned_text=[]
    for sentence in tqdm(data.posts):
        sentence=sentence.lower()
        
#         removing links from text data
        sentence=re.sub('https?://[^\s<>"]+|www\.[^\s<>"]+',' ',sentence)
    
#         removing other symbols
        sentence=re.sub('[^0-9a-z]',' ',sentence)
    
        
        data_length.append(len(sentence.split()))
        cleaned_text.append(sentence)
    return cleaned_text,data_length

    

def main(text):
    # Load your model and other necessary components
    model_xgb = load('model/model_xgb.joblib')
    vectorizer = load('model/tfidf_vectorizer.joblib')

    # Process your input data
    # Assume 'sentence' is the text input you are classifying
    preprocessed_text = pre_process_sentence(text)
    vectorized_text = vectorizer.transform([preprocessed_text])

    # Make a prediction
    predicted_class = model_xgb.predict(vectorized_text)

    # Translate the numeric prediction to MBTI type
    predicted_mbti = translate_prediction_to_mbti(predicted_class, mbti_mapping)
    return "Predicted MBTI type:" + predicted_mbti

# if __name__ == "__main__":

