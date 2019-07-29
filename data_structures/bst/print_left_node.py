class Node():

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def print_leaves(root):

    def dfs(node):
        if not node.left and not node.right:
            yield node.val
        yield from dfs(node.left)
        yield from dfs(node.right)

    return list(dfs(root))
