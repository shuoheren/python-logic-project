def noMoreThanOnce(x1,x2,x3):
    if ((not x1) and (not x2) and (not x3)):
        return True
    if (x1 and not x2 and not x3):
        return True
    if (not x1 and x2 and x3):
        return True
    if (not x1 and not x2 and x3):
        return True
    return False
def atLeastOnce(x1,x2,x3):
    if (not x1 and not x2 and not x3):
        return False
    return True
def exactlyOnce(x1,x2,x3):
    if (x1 and not x2 and not x3):
        return True
    if (not x1 and x2 and not x3):
        return True
    if (not x1 and not x2 and x3):
        return True
    return False
def differentTimeSlots(x1,x2,x3,y1,y2,y3):
    if not atLeastOnce(x1,x2,x3) or not atLeastOnce(y1,y2,y3):
        return True
    if exactlyOnce(x1,x2,x3) and exactlyOnce(y1,y2,y3):
        if ((x1==y1)and (x2==y2) and (x3==y3)):
            return False
    return True

def isItValid(a1,a2,a3,b1,b2,b3,c1,c2,c3,d1,d2,d3,e1,e2,e3,f1,f2,f3):
    # they can't be put together:
    # (A, B), (A, C), (A, D), (B, E), (C,E),(C,D),(D,F),(B,F)
    if not differentTimeSlots(a1,a2,a3,b1,b2,b3):# (A,B)
        return False
    if not differentTimeSlots(a1,a2,a3,c1,c2,c3):# (A,C)
        return False
    if not differentTimeSlots(a1,a2,a3,d1,d2,d3):# (A,D)
        return False
    if not differentTimeSlots(b1,b2,b3,e1,e2,e3):# (B,E)
        return False
    if not differentTimeSlots(c1,c2,c3,e1,e2,e3):# (C,E)
        return False
    if not differentTimeSlots(c1,c2,c3,d1,d2,d3):# (C,D)
        return False
    if not differentTimeSlots(d1,d2,d3,f1,f2,f3):# (D,F)
        return False
    if not differentTimeSlots(b1,b2,b3,f1,f2,f3):# (B,F)
        return False
    return True