"""
Check if a given binary tree is perfect or not
"""

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_depth(node):
    d = 0
    while node:
        d += 1
        node = node.left
    return d


def is_perfect_util(root, d, level=0):
    if not root:
        return True

    if not root.left and not root.right:
        return d == level + 1

    if not root.left or not root.right:
        return False

    return is_perfect_util(root.left, d, level+1) and is_perfect_util(root.right, d, level+1)


def is_perfect(root):
    depth = find_depth(root)
    return is_perfect_util(root, depth)
    

root = Node(10) 
root.left = Node(20) 
root.right = Node(30) 
root.left.left = Node(40) 
root.left.right = Node(50) 
root.right.left = Node(60) 
root.right.right = Node(70)

print(is_perfect(root))