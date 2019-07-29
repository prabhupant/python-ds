class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# get the middle of the array and make it root.
# middle of the left becomes left child
# middle of the right becomes right child

def sorted_array_to_bst(arr):

    if not arr:
        return None

    mid = len(arr)//2

    root = Node(arr[mid])

    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid+1:])
    return root


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


arr = [1,2,3,4,5,6,7,8,9]
root = sorted_array_to_bst(arr)
inorder(root)
