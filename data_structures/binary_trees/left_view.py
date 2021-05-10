"""
Print left view of a binary tree
"""

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def left_view_util(root, max_level, level):
    if not root:
        return
    
    if max_level[0] < level:
        print(root.val)
        max_level[0] = level

    left_view_util(root.left, max_level, level+1)
    left_view_util(root.right, max_level, level+1)
    

def left_view(root):
    max_level = [0]
    left_view_util(root, max_level, 1)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(5)
root.left.left.left.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8)
left_view(root)