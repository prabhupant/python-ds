class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Depth First Search
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)


def preorder(root):
    if root:
        print(root.val)
        postorder(root.left)
        postorder(root.right)


root = Node(3)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(1)
root.right.right = Node(5)

inorder(root)


