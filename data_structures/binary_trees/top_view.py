"""
Print the top view of a binary tree

Almost like vertical traversal
"""

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.col = None


def top_view(root):
    if not root:
        return

    queue = []
    col = 0
    d = {}

    queue.append(root)
    root.col = col

    while queue:
        root = queue.pop(0)
        col = root.col

        if col not in d:
            d[col] = root.val
        
        if root.left:
            queue.append(root.left)
            root.left.col = col - 1
        if root.right:
            queue.append(root.right)
            root.right.col = col + 1

    for i in sorted(d):
        print(d[i], end=" ")
        

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)

top_view(root)