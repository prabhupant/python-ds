class Node():

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def trim(root, L, R):
    if not root:
        return None
    if root.val > R:
        return trim(root.left, L, R)
    if root.val < L:
        return trim(root. right, L, R)
    root.left = trim(root.left, L, R)
    root.right = trim(root.right, L, R)
    return root
