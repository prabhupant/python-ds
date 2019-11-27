class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_k(root, k):
    if root is None:
        return
    if k == 0:
        print(root.val)
    else:
        print_k(root.left, k-1)
        print_k(root.right, k-1)
