# A full binary tree is one which has 0 or 2 children only

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check(root):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return check(root.left) and check(root.right)

    return False

