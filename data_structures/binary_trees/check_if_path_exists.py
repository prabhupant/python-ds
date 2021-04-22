"""
Given a path in an array form, check if this path leads to a leaf node

"""
class Node:

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def check_path(root, arr, n, index):
    if root is None:
        return n == 0

    if root.left == None and root.right == None and root.val == arr[index] and index == n -1:
        return True

    return (index < n) and (root.val == arr[index]) and (check_path(root.left, arr, n, index + 1) or check_path(root.right, arr, n, index + 1))
