class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def store_inorder(root, inorder):
    if root is None:
        return

    store_inorder(root.left, inorder)
    inorder.append(root.data)
    store_inorder(root.right, inorder)


def count_nodes(root):
    if root is None:
        return 0
    return count_nodes(root.left) + count_nodes(root.right) + 1


def array_to_bst(arr, root):
    if root is None:
        return
    array_to_bst(arr, root.left)
    root.data = arr[0]
    arr.pop(0)
    array_to_bst(arr, root.right)


def bt_to_bst(root):
    if root is None:
        return

    n = count_nodes(root)
    arr = []
    store_inorder(root, arr)
    arr.sort()
    array_to_bst(arr, root)

