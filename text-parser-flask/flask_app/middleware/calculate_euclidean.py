# from spacy import word2vec
from math import sqrt, pow, exp
import pandas as pd
from seaborn import heatmap
import matplotlib as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


def squared_sum(x):
    # return 3 rounded square rooted value
    return round(sqrt(sum([a * a for a in x])), 3)


def euclidean_distance(x, y):
    # return euclidean distance between two lists
    return sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))


# convert distance to a ration 0-1
def distance_to_similarity(distance):
    return 1 / exp(distance)


# ----------------------------------------------------------------
# embeddings = [nlp(sentence).vector for sentence in sentences]

# distance = euclidean_distance(embeddings[0], embeddings[1])

# # prints distance between sentences without
# print(distance)

# distance_to_similarity(distance)

# --------------------------------------------------------------TF-IDF VECTORIZER-------
