def jaccard_similarity(str1, str2):
    str1 = str1.strip()
    str2 = str2.strip()

    venn_intersection = len(set.intersection(*[set(str1), set(str2)]))

    venn_union = len(set.union(*[set(str1), set(str2)]))

    result = venn_intersection / float(venn_union)

    return result * 100
