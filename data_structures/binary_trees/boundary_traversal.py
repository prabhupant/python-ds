"""
Print the boundary traversal of a binary tree

Boundary traversal - root, left (top-down), bottom, right (bottom-up)
"""

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_leaves(root):
    if root:
        print_leaves(root.left)

        if not root.left and not root.right:
            print(root.val, end=' ')

        print_leaves(root.right)


def print_left_boundary(root):
    if root:
        if root.left:
            print(root.val, end=' ')
            print_left_boundary(root.left)
        
        elif root.right:
            print(root.val, end=' ')
            print_left_boundary(root.right)


def print_right_boundary(root):
    """
    The traversal here will be from top to bottom because 
    this will be called after finishing the left side which is 
    top-to-bottom traversal
    """
    if root:
        if root.right:
            print_right_boundary(root.right)
            print(root.val, end=' ')
        
        elif root.left:
            print_right_boundary(root.left)
            print(root.val, end=' ')


def print_boundary(root):
    if root:
        print(root.val)
        print_left_boundary(root.left)
        print_leaves(root.left)
        print_leaves(root.right)
        print_right_boundary(root.right)


root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
print_boundary(root)