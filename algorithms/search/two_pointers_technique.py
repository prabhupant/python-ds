"""
Two Pointers Technique  algorithm
Complexity = O(N)
Returns two pairs that match a specific sum in a sorted array.
For example, if the array is [1,2,3,4,5] and the sum user searches for is 8.
The program will return  [3,5], the algorithm works by assigning two pointers(indexes)
to the array, pointer in the first place and pointer in the last place, and check the
sum of two elements at the pointer, if the sum of two elements is greater than specific sum
the last pointer is decremented, if it's smaller the first element is incremented, till we
find the value we looks for.
"""

def two_pointers(numbers, value):
    first_index = 0
    second_index = len(numbers)-1
    while first_index < second_index:
        if numbers[first_index] + numbers[second_index] > value:
            second_index = second_index-1
        elif numbers[first_index] + numbers[second_index] < value:
            first_index = first_index+1
        else:
            return [numbers[first_index], numbers[second_index]]
    return -1

"""
Test Cases
"""
print(two_pointers([1, 2, 3, 4, 5], 8))
print(two_pointers([1, 7, 9, 10, 20], 27))
print(two_pointers([1, 7, 9, 10, 20], 34))
print(two_pointers([10, 7, 9, 10, 20], 20))
