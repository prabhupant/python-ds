class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def ceil(root, key):
    if not root:
        return -1
    if root.val == key:
        return root.val
    if root.val < key:
        return ceil(root.right, key)
    val = ceil(root.left, key)
    return val if val >= key else root.key


