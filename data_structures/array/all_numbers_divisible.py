# Q - Find a number in the array such that all the elements
# in the array are divisible by it

# A - just find the minimum in the array and check if all the other elements
# are divisble by it

import sys

def check(arr):
    minimum = sys.maxsize
    for i in arr:
        if i < minimum:
            minimum = i
    for i in arr:
        if not i % minimum == 0:
            return False
    return True


arr = [20,10,15,5,100,200, 201]

print(check(arr))
