from math import floor
from flask_app.middleware.text_normalize_class import Text_normalize


class Jaccard_similarity(Text_normalize):
    @staticmethod
    def calculate_jaccard_similarity(sent):
        venn_intersection = len(set.intersection(*[set(sent[0]), set(sent[1])]))
        venn_union = len(set.union(*[set(sent[0]), set(sent[1])]))
        result = venn_intersection / float(venn_union)
        return floor(result * 100)


def jaccard_similarity_prep(str1, str2):
    print(str1)
    print(str2)
    sentences = [str1, str2]
    for i, sent in enumerate(sentences):
        sentences[i] = Jaccard_similarity.sentence_strip(sent)
        sentences[i] = Jaccard_similarity.word_tokenize_doc(sent)
        sentences[i] = Jaccard_similarity.lower_stopword_removal(sentences[i])
        sentences[i] = Jaccard_similarity.lemmatize_doc(sentences[i])
        print(sentences[i])
        sentences[i] = Jaccard_similarity.word_tokens_to_string(sentences[i])
    print(sentences[0])
    print(sentences[1])
    return Jaccard_similarity.calculate_jaccard_similarity(sentences)
