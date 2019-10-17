"""
High Level Description:
Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

Time Complexity:
O(n)
"""


# Iterative Solution
def max_sub_array(self, arr):
    if not arr:
        return 0

    cur_sum = max_sum = arr[0]
    for num in arr[1:]:
        cur_sum = max(num, cur_sum + num)
        max_sum = max(max_sum, cur_sum)

    return max_sum
