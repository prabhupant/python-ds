"""
High Level Description:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Time Complexity:
O(n)
"""
# Iterative Solution
def maxSubArray(self, A):
    if not A:
        return 0

    curSum = maxSum = A[0]
    for num in A[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)

    return maxSum