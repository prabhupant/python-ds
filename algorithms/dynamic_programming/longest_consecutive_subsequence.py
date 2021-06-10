"""
Given an array of integers, find the length of the longest sub-sequence 
such that elements in the subsequence are consecutive integers, the 
consecutive numbers can be in any order.

The idea is to store all the elements in a set first. Then as we are iterating
over the array, we check two things - 
1. a number x can be a starting number in a sequence if x-1 is not present in the 
set. If this is the case, create a loop and check how many elements from x to x+j are
in the set
2. if x -1 is there in the set, do nothing as this number is not a starting element
and must have been considered in a different sequence
"""

def find_seq(arr, n):
    s = set()

    for num in arr:
        s.add(num)

    ans = 0
    elements = []

    for i in range(n):
        temp = []
        
        if arr[i] - 1 not in s:
            j = arr[i]

            while j in s:
                temp.append(j)
                j += 1

            if j - arr[i] > ans:
                ans = j - arr[i]
                elements = temp.copy()

    return ans, elements


arr = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]

ans, elements = find_seq(arr, len(arr))
print('Length - ', ans)
print('Elements - ', elements)
