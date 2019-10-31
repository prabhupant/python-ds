"""
High Level Description:
Useful when input is uniformly distributed over a range.
"""

def insertion_sort(x):
    for i in range(1, len(x)):
        t = x[i]
        j = i - 1
        while (j >= 0 and t < x[j]):
            x[j+1] = x[j]
            j -= 1
        x[j+1] = t

def bucket_sort(x):
    length = len(x)
    element_size = max(x)/length

    B = [[] for _ in range(length)]
    for i in range(length):
        j = int(x[i]/element_size)
        if j != length:
            B[j].append(x[i])
        else:
            B[length - 1].append(x[i])
 
    for i in range(length):
        insertion_sort(B[i])
 
    result = []
    for i in range(length):
        result += B[i]
 
    return result
