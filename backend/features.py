import pandas as pd
from nltk.tokenize import word_tokenize
import string
from nltk import pos_tag, ne_chunk
from gensim import corpora
from gensim.models import LdaModel
import textstat
from language_tool_python import LanguageTool
import joblib

def feature_extraction(df):

    count_vectorizer = joblib.load('ai_text_detector/app/tools/count_vectorizer_50k.pkl')
    bigram_vectorizer = joblib.load('ai_text_detector/app/tools/bigram_vectorizer_50k.pkl')
    trigram_vectorizer = joblib.load('ai_text_detector/app/tools/trigram_vectorizer_50k.pkl')
    bitri_vectorizer = joblib.load('ai_text_detector/app/tools/bitri_vectorizer_50k.pkl')

    # Basic NLP ------------------------------------------------

    df['char_count'] = df['cleaned_text'].apply(len)

    df['word_count'] = df['cleaned_text'].apply(lambda x: len(word_tokenize(x)))

    df['word_density'] = df['word_count'] / df['char_count']

    df['punctuation_count'] = df['text'].apply(punctuation_count)

    df['upper_case_count'] = df['text'].apply(upper_case_count)

    df['title_word_count'] = df['text'].apply(title_word_count)

    df[['noun_count','adv_count','verb_count','adj_count','pro_count']] = df['cleaned_text'].apply(lambda x: parts_of_speech(x))

    # Topic Modeling -------------------------------------------------------

    corpus = [text.split() for text in df['cleaned_text']]

    dictionary = corpora.Dictionary(corpus)

    corpus_bow = [dictionary.doc2bow(text) for text in corpus]

    num_topics = 20
    lda_model = LdaModel(corpus_bow, num_topics=num_topics, id2word=dictionary, passes=15)

    topic_distribution = lda_model.get_document_topics(corpus_bow)

    for topic in range(num_topics):
        df[f'topic_{topic + 1}_score'] = [next((t[1] for t in topic_dist if t[0] == topic), 0) for topic_dist in topic_distribution]

    # Readability Scores -------------------------------------------------------

    df['flesch_kincaid_score'] = df['cleaned_text'].apply(lambda x: textstat.flesch_kincaid_grade(x))

    df['flesch_score'] = df['cleaned_text'].apply(lambda x: textstat.flesch_reading_ease(x))

    df['gunning_fog_score'] = df['cleaned_text'].apply(lambda x: textstat.gunning_fog(x))

    df['coleman_liau_score'] = df['cleaned_text'].apply(lambda x: textstat.coleman_liau_index(x))

    df['dale_chall_score'] = df['cleaned_text'].apply(lambda x: textstat.dale_chall_readability_score(x))

    df['ari_score'] = df['cleaned_text'].apply(lambda x: textstat.automated_readability_index(x))

    df['linsear_write_score'] = df['cleaned_text'].apply(lambda x: textstat.linsear_write_formula(x))

    df['spache_score'] = df['cleaned_text'].apply(lambda x: textstat.spache_readability(x))

    # Named entity recognition ----------------------------------------------------
    df['ner_count'] = df['text'].apply(ner_count)

    # Text error length -----------------------------------------------------------
    df['error_length'] = df['text'].apply(error_length)

    # Preprocessing again --------------------------------------------------------------

    df.rename(columns={'text': 'normal_text'}, inplace=True)

    # count vectorization --------------------------------------------------------------

    # count_vectorizer = joblib.load('tools/count_vectorizer_v2.pkl')

    count_matrix = count_vectorizer.transform(df['cleaned_text'])

    feature_names = count_vectorizer.get_feature_names_out()
    count_df = pd.DataFrame(count_matrix.toarray(), columns=feature_names)
    df = pd.concat([df, count_df], axis=1)

    # bi gram vectorization --------------------------------------------------------------

    # bigram_vectorizer = joblib.load('tools/bigram_vectorizer_v2.pkl')

    bigram_matrix = bigram_vectorizer.transform(df['cleaned_text'])
    bigram_feature_names = bigram_vectorizer.get_feature_names_out()
    bigram_df = pd.DataFrame(bigram_matrix.toarray(), columns=bigram_feature_names)

    df = pd.concat([df, bigram_df], axis=1)

    # tri gram vectorization --------------------------------------------------------------
    # trigram_vectorizer = joblib.load('tools/trigram_vectorizer_v3.pkl')

    trigram_matrix = trigram_vectorizer.transform(df['cleaned_text'])
    trigram_feature_names = trigram_vectorizer.get_feature_names_out()
    trigram_df = pd.DataFrame(trigram_matrix.toarray(), columns=trigram_feature_names)

    df = pd.concat([df, trigram_df], axis=1)

    # bi tri gram vectorization --------------------------------------------------------------

    bichar_matrix = bitri_vectorizer.transform(df['cleaned_text'])

    bichar_df = pd.DataFrame(bichar_matrix.toarray(), columns=bitri_vectorizer.get_feature_names_out())

    bichar_df.columns = bichar_df.columns.str.strip()

    bichar_df = bichar_df.loc[:, ~bichar_df.columns.duplicated()]

    df = pd.concat([df, bichar_df], axis=1)

    # --------------------------------------------------------------------------------------------

    ttr_list = [len(set(word_tokenize(str(text).lower()))) / len(word_tokenize(str(text).lower())) for text in df['text']]

    ttr_df = pd.DataFrame({'lexical_diversity': ttr_list})

    df['lexical_diversity'] = ttr_df['lexical_diversity']

    return df


def punctuation_count(text):
    return sum(1 for char in text if char in string.punctuation)

def upper_case_count(text):
    return sum(1 for char in text if char.isupper())

def title_word_count(text):
    return sum(1 for word in text.split() if word.istitle())

def parts_of_speech(text):
    pos_tags = pos_tag(word_tokenize(text))
    
    noun_count = sum(1 for tag in pos_tags if tag[1] in ['NN', 'NNS', 'NNP', 'NNPS'])
    adv_count = sum(1 for tag in pos_tags if tag[1] in ['RB', 'RBR', 'RBS'])
    verb_count = sum(1 for tag in pos_tags if tag[1] in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'])
    adj_count = sum(1 for tag in pos_tags if tag[1] in ['JJ', 'JJR', 'JJS'])
    pro_count = sum(1 for tag in pos_tags if tag[1] in ['PRP', 'PRP$', 'WP', 'WP$'])
    return pd.Series([noun_count, adv_count, verb_count, adj_count, pro_count], index=['noun_count','adv_count','verb_count','adj_count','pro_count'])

def ner_count(text):
    words = word_tokenize(text)
    pos_tags = pos_tag(words)
    ner_tags = ne_chunk(pos_tags)
    ner_count = sum(1 for chunk in ner_tags if hasattr(chunk, 'label'))
    return ner_count

def error_length(text):
    tool = LanguageTool('en-US')
    matches = tool.check(text)
    return len(matches)