"""
Check if removing an edge of a binary tree can divide 
the tree in two equal halves

Solution - Count the number of nodes, say n. Then traverse the tree
in bottom up manner and find the size of every subtree (s). Check if n - s = s
"""

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count(root):
    if not root:
        return 0
    return count(root.left) + count(root.right) + 1


def check_util(root, n):
    if root == None:
        return False
    
    # Check for root
    if count(root) == n - count(root):
        return True
    
    # Check for all the other nodes
    return check_util(root.left, n) or check_util(root.right, n)


def check(root):
    n = count(root)
    return check_util(root, n)


root = Node(5)
root.left = Node(1)
root.right = Node(6)
root.left.left = Node(3)
root.right.left = Node(7)
root.right.right = Node(4)

print(check(root))