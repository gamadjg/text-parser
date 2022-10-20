# from spacy import word2vec
import io
import base64
import pandas as pd
from seaborn import heatmap
from flask import send_file
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


def find_cosine_similarity(text1, text2):
    headlines = [
        "Investors unfazed by correction as crypto funds see $154 million inflows",
        "Bitcoin, Ethereum prices continue descent, but crypto funds see inflows",
        "The surge in euro area inflation during the pandemic: transitory but with upside risks",
        "Inflation: why it's temporary and raising interest rates will do more harm than good",
    ]
    # common
    # "Will Cryptocurrency Protect Against Inflation?",

    vectorizer = CountVectorizer()
    print(vectorizer)
    X = vectorizer.fit_transform(headlines)
    arr = X.toarray()

    result = cosine_similarity(arr)
    print(result)
    return create_heatmap(cosine_similarity(arr), headlines)


def create_heatmap(similarity, headlines=[], cmap="YlGnBu"):
    labels = [headline[:20] for headline in headlines]
    df = pd.DataFrame(similarity)
    df.columns = labels
    df.index = labels
    fig, ax = plt.subplots(figsize=(5, 5))
    fig.show()
    heatmap(df, cmap=cmap)
    canvas = FigureCanvas(fig)
    img = io.BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype="img/png")


# create_heatmap(cosine_similarity(arr))
