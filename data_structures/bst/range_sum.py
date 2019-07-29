class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def range_sum_preorder(root, L, R):
    stack = [root]
    sum = 0
    while stack:
        node = stack.pop()
        if node:
            if L <= node.val <= R:
                sum += node.val
            if L < node.val:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
    return sum


root = Node(5)
root.left = Node(3)
root.right = Node(7)

root.left.left = Node(1)
root.left.right = Node(4)

root.right.right = Node(10)
root.right.left = Node(6)

print(range_sum_preorder(root, 7, 10))
