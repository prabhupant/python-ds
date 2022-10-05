'''
Finding the next highest power of 2 to the given positve integer
'''


def findNextPowerOf2(n):
    n = n - 1
    while n & n - 1:
        n = n & n - 1
    return n << 1
