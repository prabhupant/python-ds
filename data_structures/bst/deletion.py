class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


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
            root = root.right()


def min_value_node(root):
    curr = root
    while curr.left:
        curr = curr.left
    return curr


def delete(root, val):
    if not root:
        return root

    if val < root.val:
        root.left = delete(root.left, val)
    
    elif val > root.val:
        root.right = delete(root.right, val)

    else:
        # Root with one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)

    return root



    
