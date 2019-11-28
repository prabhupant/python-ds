class Node:

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def length(root, ans):
    if not root:
        return 0

    left = length(root.left, ans)
    right = length(root.right, ans)

    left_max = 0
    right_max = 0

    if root.left and root.left.val == root.val:
        left_max += 1

    if root.right and root.right.val == root.val:
        right_max += 1

    ans[0] = max(ans[0], left_max + right_max)

    return max(left_max, right_max)


def longest_path(root):
    ans = [0]
    length(root, ans)
    return ans[0]
