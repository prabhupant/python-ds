# Find the sum of all nodes of a binary tree

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sum_nodes(root):
    if root is None:
        return 0

    return root.val + sum_nodes(root.left) + sum_nodes(root.right)
