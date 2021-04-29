"""
Create a BST such that it can have duplicate nodes.
Technically BST cannot have duplicate nodes. The work around is to
have a counter associated with every node. Increment its count whenever
there is a duplicate. If the count goes to zero, delete that node
"""


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


def min_value_node(root):
    curr = root
    while curr:
        curr = curr.left
    return curr.val


def delete(root, val):
    if not root:
        return None
    
    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        if root.count > 1:
            root.count -= 1
        else:
            # check if left node is None
            if not root.left:
                temp = root.right
                root = None
                return temp
            # chec if right node is None
            if not root.right:
                temp = root.left
                root = None
                return temp
            
            temp = min_value_node(root.right)
            root.val = temp.val
            root.right = delete(root.right, temp.val)

    return root


root = Node(5)
insert(root, 4)
insert(root, 6)
insert(root, 4)
insert(root, 8)
insert(root, 10)

inorder(root)

print("After deletion")
root = delete(root, 8)
inorder(root)