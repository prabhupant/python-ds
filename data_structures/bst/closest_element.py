import sys

class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def closest_element(root, k):
    if not root:
        return None
    curr = root
    min_diff = sys.maxsize
    element = None
    while curr:
        if curr.val == k:
            return curr.val
        if abs(curr.val - k) < min_diff:
            min_diff = abs(curr.val - k)
            element = curr.val

        if curr.val > k:
            curr = curr.left
        else:
            curr = curr.right
    return element


root = Node(5)
root.left = Node(3)
root.right = Node(10)

root.left.left = Node(2)
root.left.right = Node(4)

root.right.right = Node(20)
root.right.left = Node(8)

print(closest_element(root, 18))
