# Convert a tree that is a left right representation to a 
# down right representation

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.rigt = None


def convert(root):
    if root is None:
        return

    convert(root.left)
    convert(root.right)

    if root.left == None:
        root.left = root.right
    else:
        root.left.right = root.right

    root.right = None
