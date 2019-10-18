"""
High Level Description:
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Note:
* All numbers (including target) will be positive integers.
* The solution set must not contain duplicate combinations.
"""

def combinationSum(candidates, target):
    res = []
    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res
    
def dfs(nums, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return 
    for i in range(index, len(nums)):
        dfs(nums, target-nums[i], i, path+[nums[i]], res)

'''Usage Example'''
# candidates = [2,3,6,7]
# target = 7
# print(combinationSum(candidates, target))