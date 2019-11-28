# Find the max value in only the left nodes of the tree

# Do inorder traversal and just keep track of the values

class Node:

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def find(root):
    res = -999999999999

    if not root:
        return res

    if root.left != None:
        res = root.left.val

    return max(find(root.left), res, find(root.right))
