import sys

def three_largest(arr):
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
    print(first, second, third)


arr = [10,45,3,7,4,6,8,9,4,6,4,23,45,56,47,25,34,67,634]
three_largest(arr)

