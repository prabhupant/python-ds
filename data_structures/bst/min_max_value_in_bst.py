class Node():

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def min_value(root):
    if not root:
        return None
    curr = root
    while curr.left:
        curr = curr.left
    return curr.val


def max_value(root):
    if not root:
        return None
    curr = root
    while curr.right:
        curr = curr.right
    return curr.val


root = Node(5)
root.left = Node(3)
root.right = Node(7)

root.left.left = Node(1)
root.left.right = Node(4)

root.right.left = Node(6)

print(max_value(root))
print(min_value(root))
