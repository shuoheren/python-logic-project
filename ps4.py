def jaccard_similarity(A,B):
#inputs two sets A and B and returns the Jaccard similarity   
    lA=len(A)
    lB=len(B)
    if lA==0 and lB==0:
        return 1
    if lA==0 or lB==0:
        return 0
    intersection = {element for element in A if element in B}
    lAB = len(intersection)
    jaccard_similarity = float(lAB) / float((lA + lB - lAB))
    return jaccard_similarity

def jaccard_distance(A,B):
#inputs two sets A and B and returns the Jaccard distance
    return 1 - jaccard_similarity(A,B)

A = ['cs', 'ma', 'cs', 'ma']

B = ['cs', 'ma']
c=set()
d=set()
d.add(c)
e=set()
print(jaccard_similarity(set(e), set(d)))