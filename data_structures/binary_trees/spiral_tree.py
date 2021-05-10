"""
Do level order traversal of a tree in spiral form
"""

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def height(root):
    if not root:
        return 0
    
    lheight = height(root.left)
    rheight = height(root.right)

    return 1 + max(lheight, rheight)


def print_spiral(root):
    h = height(root)

    left_to_right = False

    for i in range(1, h+1):
        print_level(root, i, left_to_right)
        left_to_right = not left_to_right


def print_level(root, level, left_to_right):
    if not root:
        return

    if level == 1:
        print(root.val, end=' ')
    elif level > 1:
        if left_to_right:
            print_level(root.left, level-1, left_to_right)
            print_level(root.right, level-1, left_to_right)
        else:
            print_level(root.right, level-1, left_to_right)
            print_level(root.left, level-1, left_to_right)


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(7) 
root.left.right = Node(6) 
root.right.left = Node(5) 
root.right.right = Node(4) 

print_spiral(root)