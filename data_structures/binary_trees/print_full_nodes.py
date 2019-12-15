# Given a tree, print all the full nodes of it
# A full node is such that both its children are present

class Node:

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def print_full(root):
    if not root:
        return
    if root.left and root.right:
        print(root.val, end=' ')
    print_full(root.left)
    print_full(root.right)


root = Node(10)
root.left = Node(8)
root.right = Node(2)

root.left.left = Node(3)
root.left.right = Node(5)

root.right.left = Node(7)

print_full(root)
