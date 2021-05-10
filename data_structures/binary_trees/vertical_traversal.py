"""
Print vertical view of a binary tree

           1
        /    \ 
       2      3
      / \   /   \
     4   5  6   7
               /  \ 
              8   9 
               
              
The output of print this tree vertically will be:
4
2
1 5 6
3 8
7
9

source - https://www.geeksforgeeks.org/print-binary-tree-vertical-order-set-2/
"""

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.col = None


def print_vertical_util(root, col, d):
    if not root:
        return 

    if col in d:
        d[col].append(root.val)
    else:
        d[col] = [root.val]

    print_vertical_util(root.left, col-1, d)
    print_vertical_util(root.right, col+1, d)

    
def print_vertical(root):
    d = {}
    col = 0

    print_vertical_util(root, col, d)

    for k, v in sorted(d.items()):
        for i in v:
            print(i, end=' ')
        print()


def print_vertical_iterative(root):
    queue = []
    col = 0
    d = {}

    queue.append(root)
    root.col = col

    while queue:
        root = queue.pop(0)
        col = root.col

        if col not in d:
            d[col] = [root.val]
        else:
            d[col].append(root.val)

        if root.left:
            queue.append(root.left)
            root.left.col = col - 1
        if root.right:
            queue.append(root.right)
            root.right.col = col + 1

    for k, v in sorted(d.items()):
        for i in v:
            print(i, end=' ')
        print()



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

print_vertical(root)

print("Iterative solution - ")
print_vertical_iterative(root)