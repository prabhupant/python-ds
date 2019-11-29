class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def no_siblings(root):
    if root is None:
        return

    if root.left is not None and root.right is not None:
        no_siblings(root.left)
        no_siblings(root.right)

    elif root.right is not None:
        print(root.right.val)
        no_siblings(root.right)

    elif root.left is not None:
        print(root.left.val)
        no_siblings(root.left)

