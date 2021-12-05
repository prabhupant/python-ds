class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    """
    Inoder Traversel(left Node,root Node,right Node)
    """
    def inorder(self,node):
        if node is not None:
           self.inorder(node.left)
           print(node.val)
           self.inorder(node.right)


root=Node(5)
root.left=Node(2)
root.right=Node(7)
root.left.left=Node(1)
root.left.right=Node(4)
t=Tree()
t.inorder(root)
