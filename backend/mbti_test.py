import re
import nltk
from nltk.stem import WordNetLemmatizer
from joblib import load
from nltk.corpus import stopwords
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder
import sklearn

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
lemmatizer = WordNetLemmatizer()
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
    words = [lemmatizer.lemmatize(word) for word in words]
    sentence = ' '.join(words)
    # Remove MBTI personality words if required
    if remove_mbti_profiles:
        sentence = re.sub(r'\b(?:' + '|'.join(unique_type_list) + r')\b', '', sentence)

    return sentence

def clear_text(data):
    data_length=[]
    lemmatizer=WordNetLemmatizer()
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

class Lemmatizer(object):
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
    def __call__(self, sentence):
        return [self.lemmatizer.lemmatize(word) for word in sentence.split() if len(word)>2]
    

def main():
    # Load your model and other necessary components
    model_xgb = load('/kaggle/input/mbti-train/model_xgb.joblib')
    vectorizer = load('/kaggle/input/mbti-train/tfidf_vectorizer.joblib')

    # Process your input data
    # Assume 'sentence' is the text input you are classifying
    sentence = """In moments of reflection, I often ponder the profound interconnectedness of our experiences and the threads of commonality that weave through our diverse narratives. It's fascinating, isn't it, how our individual journeys, each so uniquely sculpted by our dreams and struggles, somehow converge in shared moments of understanding? I believe that each interaction holds the potential for transformative insight, not just about the world around us but also the landscapes within us. This belief compels me to seek out authenticity in all my encounters, urging a deeper connection that transcends the superficial layers of conversation. It’s about nurturing a space where vulnerability meets acceptance, where we can be unapologetically ourselves and encourage others to do the same. In this space, we don’t just exchange words; we share parts of our soul, hoping to resonate, to understand, and to be understood. In doing so, we not only find others but rediscover ourselves, over and over, in every heartfelt exchange"""
    preprocessed_text = pre_process_sentence(sentence)
    vectorized_text = vectorizer.transform([preprocessed_text])

    # Make a prediction
    predicted_class = model_xgb.predict(vectorized_text)

    # Translate the numeric prediction to MBTI type
    predicted_mbti = translate_prediction_to_mbti(predicted_class, mbti_mapping)
    print("Predicted MBTI type:", predicted_mbti)

if __name__ == "__main__":
    main()