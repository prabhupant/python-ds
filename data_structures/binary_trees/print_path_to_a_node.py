class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def has_path(root, stack, x):
    if not root:
        return False

    stack.append(root.val)

    if root.val == x:
        return True

    if has_path(root.left, stack, x) or has_path(root.right, stack, x):
        return True

    stack.pop()
    return False


def print_path(root, x):
    arr = []

    if has_path(root, arr, x):
        for i in arr:
            print(i, end=' ')
    else:
        print('Path not present')
