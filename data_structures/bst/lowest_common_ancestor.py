class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lca(root, n1, n2):
    while root:
        if root.val > n1 and root.val > n2:
            root = root.left
        elif root.val < n1 and root.val < n2:
            root = root.right
        else:
            return root.val
    return root


root = Node(5)
root.left = Node(3)
root.right = Node(7)

root.left.left = Node(2)
root.left.right = Node(4)
root.left.left.left = Node(1)

root.right.right = Node(8)
root.right.left = Node(6)

print(lca(root, 2, 6))
