"""
High level explanation:
Bubble sort:
is a simple sorting algorithm that repeatedly steps through the list,
compares adjacent elements and swaps them if they are in the wrong order.
The pass through the list is repeated until the list is sorted.

Time Complexity:
Bubble sort has a time complexity of О(n^2)
"""


def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-1):
            if (arr[j] > arr[j+1]):
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr
