# Diameter of a binary tree is the longest path between two leaf nodes of a binary tree
# Diameter of a binary tree is maximum value of (left_height + right_height + 1) for each node

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def height(root, ans):
    if not root:
        return 0

    lheight = height(root.left, ans)
    rheight = height(root.right, ans)

    ans[0] = max(ans[0], 1 + lheight + rheight)

    return 1 + max(lheight, rheight)


def diameter(root):
    if not root:
        return 0

    ans = [-9999999999]

    h = height(root, ans)
    return ans[0]
