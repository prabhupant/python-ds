"""
In an input of unsorted integer array, find the number of elements
that can be searched using binary search

The idea is the an element is binary searchable if the elements to the
left of it are smaller than it and the elements to the right of it
are bigger than it

So maintain two arrays - left_max and right_min such that in i'th index -

* left_max[i] contains the max element between 0 and i-1 (left to right movement)
* right_min[i] contains the min element between i+1 and n-1 (right to left movement)

Now for every element in the array, if its index its i, then it is binary searchable 
if left_max[i] < arr[i] < right_min[i]
"""
import sys

def get_searchable_numbers(arr, n):
    left_max = [None] * n
    right_min = [None] * n

    left_max[0] = float('-inf')
    right_min[n-1] = float('inf')

    for i in range(1, n):
        left_max[i] = max(left_max[i-1], arr[i-1])

    for i in range(len(arr) - 2, -1, -1):
        right_min[i] = min(right_min[i+1], arr[i+1])

    res = []
    count = 0
    
    for i in range(0, n):
        num = arr[i]
        left = left_max[i]
        right = right_min[i]

        if left < num < right:
            res.append(num)
            count += 1

    return count, res


if __name__ == '__main__':
    #arr = [5,1,4,3,6,8,10,7,9]
    arr = [4,1,3,9,8,10,11]
    count, res = get_searchable_numbers(arr, len(arr))

    print(count, res)
