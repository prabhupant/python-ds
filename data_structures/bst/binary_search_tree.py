class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST():

    def __init__(self):
        self.root = Node(None)


    def insert(self, new_data):
        if self.root is None:
            self.root = Node(new_data)
        else:
            if self.root.val < new_data:

                self.insert(self.root.right, new_data)
            else:
                self.insert(self.root.left, new_data)


    def inorder(self):
        if self.root:
            self.inorder(self.root.left)
            print(self.root.val)
            self.inorder(self.root.right)


if __name__ == '__main__':
    tree = BST()
    tree.insert(5)
    tree.insert(4)
    tree.insert(7)
    tree.inorder()
