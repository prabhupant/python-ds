class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def increasing_bst(root):
    def inorder(node):
        if node:
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)
    ans = curr = Node(None)
    for v in inorder(root):
        curr.right = Node(v)
        curr = curr.right
    return ans.right
