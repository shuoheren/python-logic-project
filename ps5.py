def notAntiReflexive_and_notReflexive(a,r):
    return (not Reflexive(a,r)) and (not AntiReflexive(a,r))
def Reflexive(a,r):
    for x in a:
        if not r(x,x):
            return False
    return True

def AntiReflexive(a,r):
    for x in a:
        if r(x,x):
            return False
    return True

def surjective(a,b,f):
    if len(a)<len(b):
        return False
    expected_ranges={}
    for element in b:
        expected_ranges[element]=0
    for input in a:
        if f(input) in expected_ranges:
            expected_ranges[f(input)]=1
        else:
            return False
    for element in expected_ranges:
        if expected_ranges[element]==0:
            return False

    return True
