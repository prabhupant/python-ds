# Check if two nodes are cousin or not

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level(root, node, lev):
    if not root:
        return 0
    if root == node:
        return lev

    l = level(root.left, node, lev + 1)
    
    if not l == 0:
        return l

    l = level(root.right, node, lev + 1)


def is_sibling(root, a, b):
    if root is None:
        return 0

    return ( (root.left == a and root.right == b) or (root.left == b and root.right == a) or is_sibling(root.left, a, b) or is_sibling(root.right, a, b) )


def is_cousin(root, a, b):
    if level(root, a, 1) == level(root, b, 1) and not is_sibling(root, a, b):
        return True
    else:
        return False
