class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def reverse_inorder(root):
    if not root:
        return None
    stack = []
    arr = []
    while True:
        if root:
            stack.append(root)
            root = root.right
        else:
            if not stack:
                break
            root = stack.pop()
            arr.append(root.val)
            root = root.left
    return arr


root = Node(5)
root.left = Node(3)
root.right = Node(7)

root.left.left = Node(2)
root.left.right = Node(4)

root.right.right = Node(8)
root.right.left = Node(6)

lst = reverse_inorder(root)
print(lst)

