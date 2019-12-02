# Find the largest subtree sum in a binary tree
# Do a postorder traversal

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sum_util(root, ans):
    if root is None:
        return 0

    s = root.val + sum_util(root.left, ans) + sum_util(root.right, ans)

    ans[0] = max(ans[0], s)

    return s


def find_sum(root):
    if root is None:
        return 0

    ans = [-99999999]

    sum_util(root, ans)

    return ans[0]
