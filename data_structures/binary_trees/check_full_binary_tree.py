"""
A full binary tree is a tree which has either 0 children or 2 children
"""

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check(root):
    if not root:
        return True

    if not root.left and not root.right:
        return True

    if root.left and root.right:
        return check(root.left) and check(root.right)


root = Node(0)
root.left = Node(1)
root.right = Node(2)

if check(root):
    print('True')
else:
    print("False")