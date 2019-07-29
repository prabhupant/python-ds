class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return None
    stack = []

    # Keep adding left until there is none
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


def postorder(root):
    if not root:
        return None
    stack = []
    curr = root
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            temp = stack[-1].right
            if not temp:
                temp = stack.pop()
                print(temp.val, end=" ")
                while stack and temp == stack[-1].right:
                    temp = stack.pop()
                    print(temp.val, end=" ")
            else:
                curr = temp


def preorder(root):
    if not root:
        return None
    stack = [root]
    while stack:
        root = stack.pop()
        print(root.val, end=" ")
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)


root = Node(5)
root.left = Node(2)
root.right = Node(7)

root.left.left = Node(1)
root.left.right = Node(3)

root.right.right = Node(8)
root.right.left = Node(6)

#inorder(root)
#preorder(root)
postorder(root)
