"""
Quicksort Running Time:
Quick sort average case is O(n log n)
    each level takes O(n) but splitting the data is O(log n)
    O(n) * O(log n) = O(n log n)
Worse case is O(log n2)
    if pivot is smallest value, each level is O(n) and splitting the data is O(n)
    O(n) * O(n) = O(n2)
"""

# quicksort function
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

array = [100, 5, 72, 41, 80, 1, 99, 36, 27, 78]
print(quicksort(array)) # [1, 5, 27, 36, 41, 72, 78, 80, 99, 100]

