"""
Print right view of a binary tree

The idea behind using max_level[0] is that - 
1. Its value when changes will be reflected in every recursion call
2. We are visiting right side first. So this acts as a check that that level was done
"""

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def right_view_util(root, max_level, level):
    if not root:
        return
    
    if max_level[0] < level:
        print(root.val)
        max_level[0] = level

    right_view_util(root.right, max_level, level+1)
    right_view_util(root.left, max_level, level+1)


def right_view(root):
    max_level = [0]
    right_view_util(root, max_level, 1)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
right_view(root)