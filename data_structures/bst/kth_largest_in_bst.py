class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def reverse_inorder(root, k):
    if not root:
        return None
    counter = 1
    stack = []
    while True:
        if root:
            stack.append(root)
            root = root.right
        else:
            if not stack:
                break
            root = stack.pop()
            if counter == k:
                return root.val
            else:
                counter += 1
            root = root.left

    return "not enough elements in BST"


root = Node(5)
root.left = Node(3)
root.right = Node(7)

root.left.left = Node(2)
root.left.right = Node(4)

root.right.right = Node(8)
root.right.eft = Node(6)

k = int(input("Enter K : "))

ans = reverse_inorder(root, k)
print(ans)
