class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def search(root, val):
    if root is None or root.val == val:
        return root
    if root.val < val:
        return search(root.left, val)
    else:
        return search(root.right, val)


def search_iterative(root, val):
    while root:
        if val > root.val:
            root = root.right
        elif val < root.val:
            root = root.left
        else:
            return True
    return False
