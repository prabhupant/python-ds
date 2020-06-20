"""
Bubble Sort worst time complexity occurs when array is reverse sorted - O(n^2)
Best time scenario is when array is already sorted - O(n)
"""

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j] 
    return array


def bubble_sort_optimized(array):
    """
    Optimizes on bubble sort by taking care of already swapped cases
    Reference - https://github.com/prabhupant/python-ds/pull/346
    """
    has_swapped = True

    num_of_iterations = 0

    while has_swapped:
        has_swapped = False
        for i in range(len(array) - num_of_iterations - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                has_swapped = True
        num_of_iterations += 1
