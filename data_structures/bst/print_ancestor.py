class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_ancestor_recursive(root, key):
    if not root:
        return False
    if root.val == key:
        return True
    if print_ancestor_recursive(root.left, key) or print_ancestor_recursive(root.right, key):
        return root.data
    return False



