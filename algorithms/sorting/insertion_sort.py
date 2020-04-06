"""
High Level Description:
For every element in the given list, find its correct index by iterating
backwards and finding a slot. This forms a sorted array.
Time Complexity:
Every element is visited, which contributes O(n). Swapping backwards takes
O(n/2) time on average, meaning that the total complexity is O(n^2)
"""

def insertion_sort(lst):
    for i in range(1,len(lst)):
        while(i > 0 and lst[i] < lst[i - 1]):
            lst[i], lst[i - 1] = lst[i -  1], lst[i]
            i -= 1
    return lst

test_data  = [5,9,4,27,3,6]
print(insertion_sort(test_data))

test_data  = ['f','b','z','a','x']
print(insertion_sort(test_data))

# Resulting output:
# [3, 4, 5, 6, 9, 27]
# ['a', 'b', 'f', 'x', 'z']
