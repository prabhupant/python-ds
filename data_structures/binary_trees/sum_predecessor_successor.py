# Convert a binary tree such that each node is the sum of 
# its inorder predecessor and successor

# Store the inorder traversal in an array. Now while traversing
# replace each node with the values arr[i-1] + arr[i+1] as these
# are the inorder predecessor and successor

class Node:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    if not root:
        return None

    arr = []
    stack = []

    while True:
        if root:
            stack.append(root)
            root = root.left
        else:
            if not stack:
                break
            root = stack.pop()
            arr.append(root.val)
            root = root.right

    return arr


def replace_nodes(root, arr):
    if not root:
        return 
    
    stack = []
    i = 1
    while True:
        if root:
            stack.append(root)
            root = root.left
        else:
            if not stack:
                break
            root = stack.pop()
            root.val = arr[i-1] + arr[i+1]
            i += 1
            root = root.right


    return root


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)
root.right.left = Node(6)

arr = inorder(root)
print('Inorder traversal original - ', arr)

new_root = replace_nodes(root, arr)
new_arr = inorder(new_root)
print('New traversal - ', new_arr)

