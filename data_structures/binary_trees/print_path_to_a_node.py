class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def has_path(root, arr, x):
    if not root:
        return False

    arr.append(root.val)

    if root.val == x:
        return True

    if has_path(root.left, arr, x) or has_path(root.right, arr, x):
        return True

    # If the required node is not in the left or right subtree, remove 
    # the parent node from where the fork starts
    arr.pop()
    return False


def print_path(root, x):
    arr = []

    if has_path(root, arr, x):
        for i in arr:
            print(i, end=' ')
    else:
        print('Path not present')
