#Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

##  1
## / \
##2   3
##   / \
##  4   5


class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def print_(self):
        print(self.val)
        if self.left:
            self.left.print_()
        if self.right:
            self.right.print_()

            
# Tests
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.left = b
a.right = c
c.left = d
c.right = e

a.print_()        
