# A continuous tree is such that the absolute difference between two
# adjacent nodes is 1

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def continuous(root):
    # Can be continuous if 
    # 1. Root is none
    # 2. Both left and right STs are none
    # 3. If left ST is none, check for right
    # 4. If right ST is none, check for left
    # 5. Else check for everything

    if root is None:
        return True
    
    if root.left == None and root.right == None:
        return True

    if root.left == None:
        return (abs(root.val - root.right.val) == 1) and continuous(root.right)

    if root.right == None:
        return (abs(root.val - root.left.val) == 1) and continuous(root.left)

    return (abs(root.val - root.right.val) == 1) and (abs(root.left.val - root.val) == 1) and continuous(root.left) and continuous(root.right)

