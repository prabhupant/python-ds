class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST():

    def __init__(self,root=None):
        self.root = root


    def insert(self, current_node,new_data):
        if self.root is None:
            self.root = Node(new_data)
        else:
            if current_node.val < new_data:
                if current_node.right == None:
                    current_node.right = Node(new_data)
                else:
                    self.insert(current_node.right, new_data)

            elif current_node.val > new_data:
                if current_node.left == None:
                    current_node.left = Node(new_data)
                else:
                    self.insert(current_node.left,new_data)


    def inorder(self,node):
        if node is not None:
            self.inorder(node.left)
            print(node.val)
            self.inorder(node.right)


if __name__ == '__main__':
    tree = BST()
    tree.insert(tree.root,5)
    tree.insert(tree.root,4)
    tree.insert(tree.root,7)
    tree.inorder(tree.root)
