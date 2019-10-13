class Tree:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: Tree) -> bool:
        
        def check(node):
            if not node:
                return 0
            
            left = check(node.left)
            right = check(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)
        
        return check(root) != -1
        