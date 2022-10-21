from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize.treebank import TreebankWordDetokenizer


class Text_normalize:
    @staticmethod
    def sent_tokenize_doc(doc):
        return sent_tokenize(doc)

    @staticmethod
    def word_tokenize_doc(doc):
        return word_tokenize(doc)

    @staticmethod
    def make_lower(doc):
        for i, value in enumerate(doc):
            doc[i] = value.lower()
        return doc

    @staticmethod
    def lower_stopword_removal(doc):
        stop_words = set(stopwords.words("english"))
        filtered_tokens = []
        for word in doc:
            if word not in stop_words:
                filtered_tokens.append(word.lower())
        return filtered_tokens

    @staticmethod
    def lemmatize_doc(doc):
        wnl = WordNetLemmatizer()
        lemmatized_tokens = [wnl.lemmatize(w) for w in doc]
        return lemmatized_tokens

    @staticmethod
    def word_tokens_to_string(doc):
        return TreebankWordDetokenizer().detokenize(doc)

    @staticmethod
    def sentence_strip(doc):
        return doc.strip()
