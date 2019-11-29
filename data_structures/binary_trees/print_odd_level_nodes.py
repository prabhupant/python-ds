# Print all the nodes at odd levels of a binary tree

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_odd(root, is_odd=True):
    if not root:
        return

    if is_odd:
        print(root.val, end=' ')

    print_odd(root, not is_odd)
    print_odd(root, not is_odd)
