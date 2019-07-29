class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def height(root, ans):
    if not root:
        return 0
    lheight = height(root.left, ans)
    rheight = height(root.right, ans)

    # Diameter is basically the max of (1 + lheight + rheight)
    # So we are storing it here to reduce calling it again
    # O(n)
    ans[0] = max(ans[0], 1 + lheight + rheight)

    return 1 + max(lheight, rheight)


def diameter(root):
    if not root:
        return 0
    ans =[-99999999999]
    h = height(root, ans)
    return ans[0]


if __name__ == '__main__':

    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.right = Node(8)
    root.right.left  = Node(6)
    print(diameter(root))
