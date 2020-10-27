# Q - Find the max product of three elements of an array
# A - Find the max 3 numbers and 2 min numbers. Then find the max of (min1*min2*max1, max1*max2*max3)

import sys

def product(arr):
    min1 = sys.maxsize
    min2 = sys.maxsize
    max1 = -sys.maxsize
    max2 = -sys.maxsize
    max3 = -sys.maxsize

    for n in arr:
        if n <= min1:
            min2 = min1
            min1 = n
        elif n <= min2:
            min2 = n

        if n >= max1:
            max3 = max2
            max2 = max1
            max1 = n
        elif n >= max2:
            max3 = max2
            max2 = n
        elif n >= max3:
            max3 = n

    return max(min1*min2*max1, max1*max2*max3)
            
