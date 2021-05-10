"""
Check if two nodes are cousin or not

Condition for being cousin - 
1. Level is same
2. They are not siblings

"""

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level(root, node, lev):
    if not root:
        return 0

    if root == node:
        return lev

    l = level(root.left, node, lev+1)

    if not l == 0:
        return l

    l = level(root.right, node, lev+1)


def is_sibling(root, a, b):
    if not root:
        return False

    return (root.left == a and root.right == b) or \
        (root.right == b and root.left == a) or \
        is_sibling(root.left, a, b) or \
        is_sibling(root.right, a, b)


def is_cousin(root, a, b):
    if level(root, a, 1) == level(root, b, 1) and not is_sibling(root, a, b):
        return True
    else:
        return False


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(15)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
  
node1 = root.left.right
node2 = root.right.right 

print(is_cousin(root, node1, node2))