class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1


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
            print(root.val, "(", root.count, ")")
            root = root.right


def insert(root, val):
    if not root:
        return Node(val)
    
    if val == root.val:
        root.count += 1
        return root
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


def delete(root, val):
    if not root:
        return
    if root.val == val:
        if root.count > 1:
            root.count -= 1


root = Node(5)
insert(root, 4)
insert(root, 6)
insert(root, 4)
insert(root, 8)
insert(root, 10)

inorder(root)
