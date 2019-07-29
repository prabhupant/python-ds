class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    new_node = Node(val)
    parent = None
    curr = root
    while curr:
        parent = curr
        if curr.val <= val:
            curr = curr.right
        else:
            curr = curr.left

    if parent.val <= val:
        parent.right = new_node
    else:
        parent.left = new_node


def inorder(root):
    if not root:
        return None
    stack = []
    while True:
        if root:
            stack.append(root)
            root = root.left
        else:
            if not stack:
                break
            root = stack.pop()
            print(root.val, end=" ")
            root = root.right


root = Node(4)
insert(root, 2)
insert(root, 6)
insert(root, 1)
insert(root, 8)
inorder(root)
