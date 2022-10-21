import warnings

data = "All work and no play makes jack dull boy. All work and no play is making David into a night owl."

# ------------------------------------------------------------------------TOKENIZE TEXT
from nltk.tokenize import sent_tokenize, word_tokenize

# break down the paragraphs of text into an array of sentence tokens
# phrases = sent_tokenize(data)
# print(phrases)

# break down the paragraphs of text into and array of word tokens (special characters qualify as their own entry)
words = word_tokenize(data)
print(words)

# -------------------------------------------------------------------------STOPWORD REMOVAL
from nltk.corpus import stopwords

# Generate a set of unique english stopwords
stop_words = set(stopwords.words("english"))
# print(stop_words)

# Filter out stopwords from our tokens
filtered_tokens = []
for w in words:
    if w not in stop_words:
        filtered_tokens.append(w.lower())

print(filtered_tokens)

# --------------------------------------------------------------------------LEMMATIZATION
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download("wordnet")
nltk.download("omw-1.4")
wnl = WordNetLemmatizer()


lemmatized_tokens = [wnl.lemmatize(w) for w in filtered_tokens]
print(lemmatized_tokens)

# --------------------------------------------------------------------------CREATE CBOW MODEL
# import gensim
# from gensim.models import Word2Vec

# model1 = Word2Vec(lemmatized_tokens, min_count=1, vector_size=100, window=5)

from sentence_transformers import SentenceTransformer
import numpy as np


def cosine_similarity(sentence_embeddings, ind_a, ind_b):
    s = sentence_embeddings

    return np.dot(s[ind_a], s[ind_b]) / (
        np.linalg.norm(s[ind_a]) * np.linalg.norm(s[ind_b])
    )
    # return np.dot(s[ind_a], s[ind_b]) / (np.linalg.norm(s[ind_a]) * np.linalg.norm(s[ind_b]))


sentences = [
    "All work and no play makes jack dull boy.",
    "All work and no play is making David into a night owl.",
]

model = SentenceTransformer("sentence-transformers/bert-base-nli-mean-tokens")
sentence_embeddings = model.encode(sentences)
s = sentence_embeddings
result = cosine_similarity(sentence_embeddings, 0, 1)

print("Result: " + str(result) + "\n" + sentences[0] + "<-->" + sentences[1])

# print(
#     f"{sentences[0]} <--> {sentences[1]}: {cosine_similarity(sentence_embeddings, 0, 1)}"
# )

# s0 = "our president is a good leader he will not fail"
# s1 = "our president is not a good leader he will fail"
# s2 = "our president is a good leader"
# s3 = "our president will succeed"

# sentences = [s0, s1, s2, s3]


# print(f"{s0} <--> {s2}: {cosine_similarity(sentence_embeddings, 0, 2)}")
# print(f"{s0} <--> {s3}: {cosine_similarity(sentence_embeddings, 0, 3)}")


# # Reads ‘alice.txt’ file
# sample = open("alice.txt", "utf8")
# s = sample.read()

# # Replaces escape character with space
# f = s.replace("\n", " ")

# data = []

# # iterate through each sentence in the file
# for i in sent_tokenize(f):
#     temp = []

#     # tokenize the sentence into words
#     for j in word_tokenize(i):
#         temp.append(j.lower())

#     data.append(temp)

# # Create CBOW model
# model1 = gensim.models.Word2Vec(data, min_count=1, vector_size=100, window=5)

# # Print results
# print(
#     "Cosine similarity between 'alice' " + "and 'wonderland' - CBOW : ",
#     model1.wv.similarity("alice", "wonderland"),
# )

# print(
#     "Cosine similarity between 'alice' " + "and 'machines' - CBOW : ",
#     model1.wv.similarity("alice", "machines"),
# )

# # Create Skip Gram model
# model2 = gensim.models.Word2Vec(data, min_count=1, vector_size=100, window=5, sg=1)

# # Print results
# print(
#     "Cosine similarity between 'alice' " + "and 'wonderland' - Skip Gram : ",
#     model2.wv.similarity("alice", "wonderland"),
# )

# print(
#     "Cosine similarity between 'alice' " + "and 'machines' - Skip Gram : ",
#     model2.wv.similarity("alice", "machines"),
# )
