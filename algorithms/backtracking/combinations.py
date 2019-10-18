"""
High Level Description:
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Time Complexity:
O(2^n)
"""

def combine(n, k):
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in combine(i-1, k-1)]

'''Usage Example'''
# print(combine(5,3))