"""
High Level Description:
For every element in the given list, find its correct index by iterating
backwards and finding a slot. This forms a sorted array.
Time Complexity:
Every element is visited, which contributes O(n). Swapping backwards takes
O(n/2) time on average, meaning that the total complexity is O(n^2)
"""

def insertion_sort(lst):
    for i, _ in enumerate(lst):
        j = i
        while(j > 0 and lst[i] < lst[j]):
            j -= 1
        lst[j], lst[i] = lst[i], lst[j]
    return lst
