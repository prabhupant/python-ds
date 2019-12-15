# Traverse the tree in preorder fashion
# append value in stack
# if root.left and root.right is None, then print all stack values
# traverse left
# traverse right
# pop from stack

class Node:

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def print_route(root, stack):
    if root == None:
        return 

    stack.append(root.val)
    if root.left == None and root.right == None:
        for i in stack:
            print(i, end=' ')
        print()

    print_route(root.left, stack)
    print_route(root.right, stack)
    stack.pop()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print_route(root, [])
