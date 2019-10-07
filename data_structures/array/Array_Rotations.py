"""
Array Rotations:-

Given an array, rotate the elements of the array without using the temp array.

Solution:-
 Rotate the given array one at a time, and then call the rotation function n times,(n being the times rotated)
 
Note:- Code using the temp array is also given.
"""

#==================== Method 1: Using Temp array to do so, takes O(n) time.======================

# def rotations(L, N, D):
#     temp = []

#     for a in range(0, d):
#         temp.append(L[a])

#     for a in range(0, n-d):
#         L[a] = L[a+d]

#     for a in range(0, d):
#         L.append(temp[a])

#     print(L)



# n=8
# d=3
# rotations(L, n ,d)

# ============ Method 2, rotate by one element at a time.==============


def rotateLeft(arr):
    temp = arr[0]
    length = len(arr)

    for item in range(0, length-1):
        arr[item] = arr[item+1]
    arr[item+1] = temp

    return arr


def rotations(arr, n):
    for a in range(0, n):
        rotateLeft(arr)
    printRotations(arr)


def printRotations(arr):
    for a in arr:
        print(a,"",end = "")

L = [1, 2, 3, 4, 5, 6, 7, 8]
rotations(L, 3)


