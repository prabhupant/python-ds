# Check if two trees are identical or not

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def identical(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None:
        return root1.val == root2. val and identical(root1.left, root2.left) and identical(root1.right, root2.right)

    return False
