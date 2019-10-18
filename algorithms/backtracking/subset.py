"""
High Level Description:
Given a set of distinct integers, S, return all possible subsets.

Time Complexity:
O(2^n)
"""

def subsets(nums):
    res = []
    dfs(sorted(nums), 0, [], res)
    return res

def dfs(nums, start, path, res):
    res.append(path)
    for i in range(start, len(nums)):
        dfs(nums, i+1, path+[nums[i]], res)

'''Usage Example'''
# S = [1, 2, 3]
# print(subsets(S))