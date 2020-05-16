"""
High level description:
Counting sort is a sorting technique based on keys between a specific range,
with efective performance on the predetermined range size of the values.   
It works by counting the number of objects having distinct key values (kind of hashing). 
Then doing some arithmetic to calculate the position of each object in the output sequence.

Time complexity:
O(n+k) where n is the number of elements in input array and k is the range of input.

Auxiliary Space: O(n+k)
"""

def counting_sort(arr):
    # Find min and max values
    min_value = min(arr)
    max_value = max(arr)

    # Count number appearances in the array
    counting_arr = [0]*(max_value-min_value+1)
    for num in arr:
        counting_arr[num-min_value] += 1
    
    # Rearrange sequence in the array
    index = 0
    for i, count in enumerate(counting_arr):
        for _ in range(count):
            arr[index] = min_value + i
            index += 1

test_array = [3, 3, 2, 6, 4, 7, 9, 7, 8]

counting_sort(test_array)

print(test_array)
