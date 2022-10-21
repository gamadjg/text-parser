from distutils.command.clean import clean
from nltk.tokenize import sent_tokenize, word_tokenize
from sentence_transformers import SentenceTransformer
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
from math import floor

stop_words = set(stopwords.words("english"))


def sent_tokenize_doc(doc):
    return sent_tokenize(doc)


def word_tokenize_doc(doc):
    return word_tokenize(doc)


def make_lower(doc):
    for i, value in enumerate(doc):
        doc[i] = value.lower()
    return doc


def lower_stopword_removal(doc):
    filtered_tokens = []
    for word in doc:
        if word not in stop_words:
            filtered_tokens.append(word.lower())
    return filtered_tokens


def lemmatize_doc(doc):
    wnl = WordNetLemmatizer()
    lemmatized_tokens = [wnl.lemmatize(w) for w in doc]
    return lemmatized_tokens


def cosine_similarity(sentences):
    model = SentenceTransformer("sentence-transformers/bert-base-nli-mean-tokens")
    sentence_embeddings = model.encode(sentences)
    s = sentence_embeddings
    return np.dot(s[0], s[1]) / (np.linalg.norm(s[0]) * np.linalg.norm(s[1]))


def cosine_prep(str1, str2):
    print(str1)
    print(str2)
    sentences = [str1, str2]
    for i, sent in enumerate(sentences):
        sentences[i] = word_tokenize_doc(sent)
        sentences[i] = lower_stopword_removal(sentences[i])
        sentences[i] = lemmatize_doc(sentences[i])
        print(sentences[i])
        sentences[i] = TreebankWordDetokenizer().detokenize(sentences[i])

    print(sentences[0])
    print(sentences[1])

    result = cosine_similarity(sentences)
    return floor(result * 100)


# st1 = "I went to the store to buy milk."
# st2 = "I went shopping for some milk!"

# print(clean_text(st1, st2))
