class Tree:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: Tree) -> bool:
        vals = set()

        def dfs(node):
            if node:
                vals.add(node.value)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return len(vals) == 1