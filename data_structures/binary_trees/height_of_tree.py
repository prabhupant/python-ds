"""
Find the height of a binary tree

Height - (max of left height and right height) + 1
"""

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def height(root):
    if not root:
        return 0

    else:
        lheight = height(root.left)
        rheight = height(root.right)

        return 1 + max(lheight, rheight)


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(7) 
root.left.right = Node(6) 
root.right.left = Node(5) 
root.right.right = Node(4) 
root.right.right.right = Node(40) 

print(height(root))