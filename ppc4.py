def jaccard_similarity(A,B):  
    if A==B:
        return 1
    if len(A)==0 or len(B)==0:
        return 0
    C = {x for x in A if x in B}
    jaccard_similarity = float(len(C)) / float((len(A) + len(B) - len(C)))
    return jaccard_similarity

def jaccard_distance(A,B):
    return 1 - jaccard_similarity(A,B)