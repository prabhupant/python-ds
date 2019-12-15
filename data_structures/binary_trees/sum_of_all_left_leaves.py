# Find the sum of all left leaves of a binary tree


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_leaf(root):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return True
    return False


def sum_left(root):
    s = 0
    stack = []

    while True:
        if root:
            stack.append(root)
            root = root.left
        else:
            if not stack:
                break
            root = stack.pop()
            if is_leaf(root.left):
                s += root.left.val
            root = root.right

    return s


root = Node(9)
root.left = Node(8)
root.right = Node(6)
root.right.left = Node(1)

root.left.left = Node(5)
root.left.right = Node(2)

print(sum_left(root))
