"""
This stupid or slow sort known also as bogo sort or monkey
sort works by shuffling the numbers in all the possible
combinations until find the sorted one
"""
import random


# Shuffle and test if it is sorted.
def permutation_sort(arr):
    n = len(arr)
    while (is_sorted(arr) is False):
        shuffle(arr)


# Check if array is sorted.
def is_sorted(arr):
    n = len(arr)
    for i in range(n-1):
        if (arr[i] > arr[i+1]):
            return False
    return True


# Shuffle the given array.
def shuffle(arr):
    n = len(arr)
    for i in range(n):
        r = random.randint(0, n-1)
        arr[i], arr[r] = arr[r], arr[i]


# test
# arr = [2, 3, 5, 0, 1, 4, 8, 9, 10]
# permutation_sort(arr)
# print("Sorted array:")
# for i in arr:
#    print(i)
