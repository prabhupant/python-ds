# check if all the leaves of a tree are at the same level

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check_util(root, level):
    if root is None:
        return True

    if root.left is None and root.right is None:
        if check.leaf_level == 0:
            check.leaf_level = level
            return True
        
        return level == check.leaf_level

    return check_util(root.left, level + 1) and check_util(root.right, level + 1)


def check(root):
    level = 0
    check.leaf_level = 0
    return check_util(root, level)
