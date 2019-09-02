import sys

def max_sum(arr):
    first = second = third = -sys.maxsize

    for i in arr:
        if i > first:
            third = second
            second = first 
            first = i
        elif i > second:
            third = second
            second = i
        elif i > third:
            third = i

    return first + second + third


arr = [1,3,6,3,6,8,3,3,7,9,4,-1,-1]

print(max_sum(arr))

