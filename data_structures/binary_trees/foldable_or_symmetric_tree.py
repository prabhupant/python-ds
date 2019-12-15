# A foldable tree is one such that the mirror of left subtree is equal
# to the right subtree

class Node:

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def foldable(left, right):
    if left is None and right is None:
        return True
    
    if left is None or right is None:
        return False

    return left.val == right.val and foldable(left.left, right.right) and foldable(left.right, right.left)


root = Node(4)

root.left = Node(2)
root.left.left = Node(1)

root.right = Node(2)
root.right.right = Node(10)

print(foldable(root.left, root.right))

