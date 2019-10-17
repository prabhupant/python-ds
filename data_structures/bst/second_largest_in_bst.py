class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_largest(root):
    curr = root
    while curr:
        if not curr.right:
            return curr.val
        curr = curr.right


def second_largest(root):
    if not root or (not root.left and not root.right):
        return "BST should have atleast 2 nodes"

    curr = root

    while curr:
        if curr.left and not curr.right:
            return find_largest(curr.left)
        
        if curr.right and not curr.right.left and not curr.right.right:
            return curr.val

        curr = curr.right


def insert(root, key):
    if root == None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    elif key > root.val:
        root.right = insert(root.right, key)
    return root


if __name__ == '__main__':
    root = Node(6)
    insert(root, 5)
    insert(root, 3)
    insert(root, 10)
    insert(root, 4)
    insert(root, 11)
    insert(root, 14)
    insert(root, 1)

    print(second_largest(root))


