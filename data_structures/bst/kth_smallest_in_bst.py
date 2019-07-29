class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root, k):
    if not root:
        return None
    stack = []
    counter = 1
    while True:
        if root:
            stack.append(root)
            root = root.left
        else:
            if not stack:
                break
            root = stack.pop()
            if counter == k:
                return root.val
            else:
                counter += 1
            root = root.right
    return "tree not big enough"


root = Node(5)
root.left = Node(3)
root.right = Node(7)

root.left.left = Node(2)
root.right.right = Node(4)

root.right.left = Node(6)
root.right.right = Node(8)

print(inorder(root, 3))

