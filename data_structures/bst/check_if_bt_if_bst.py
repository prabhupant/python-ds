import sys

MAX = sys.maxsize
MIN = -sys.maxsize

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check_BST(root, min, max):
    if root is None:
        return True

    if root.val < min or root.val > max:
        return False

    return (check_BST(root.left, min, root.val - 1) and check_BST(root.right, root.val + 1, max))

root = Node(5)
root.left = Node(4)
root.right = Node(7)

print(check_BST(root, MIN, MAX))
