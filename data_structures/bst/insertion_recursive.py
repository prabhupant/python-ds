class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insertion_recursive(root, val):
    if not root:
        return Node(val)
    else:
        if root.val < val:
            if root.right is None:
                root.right = Node(val)
            else:
                insertion_recursive(root.right, val)
        else:
            if root.left is None:
                root.left = Node(val)
            else:
                insertion_recursive(root.left, val)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)



root = Node(5)
root.left = Node(3)
root.right = Node(7)

root.left.left = Node(1)
root.left. right = Node(4)

root.right.right = Node(8)
inorder(root)
insertion_recursive(root, 6)

inorder(root)
