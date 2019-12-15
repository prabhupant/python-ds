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

# To ensure top down, print before calling for other
# To ensure bottom up, print after calling

def print_left_boundary(root):
    if root:
        if root.left:
            print(root.val, end=' ')
            print_left_boundary(root.left)

        elif root.right:
            print(root.val, end=' ')
            print_left_boundary(root.right)


def print_right_boundary(root):
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
