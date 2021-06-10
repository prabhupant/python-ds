"""
Find the longest increasing consecutive subsequence in an array

Idea - 

create a dictionary 'seq' and start iterating over the array

1. if arr[i] - 1 exists in the array, length = length + seq[arr[i] - 1]
2. else, seq[i] = 1
"""

def find_seq(arr):
    seq = {}
    count = 0

    for num in arr:
        if num - 1 in seq:
            seq[num] = seq[num - 1] + 1
            count = max(count, seq[num])
        else:
            seq[num] = 1

    return count

arr = [6, 7, 8, 3, 4, 5, 9, 10]
print(find_seq(arr))
