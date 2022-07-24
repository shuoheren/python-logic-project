def collatz_function(a):
    if a%2==0:
        return a//2
    return a*3+1

def collatz_sequence(a):
    b=a
    output=[a]
    while (b>1):
        b=collatz_function(b)
        output.append(b)
    return output


def smallest_int_with_collatz_length(n):
    length=0
    index=0
    while (length<n):
        index=index+1
        length=len(collatz_sequence(index))

    return index

#counterexample = [626331]
#for 626331 the length is 509

