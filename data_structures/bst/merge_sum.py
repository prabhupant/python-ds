class Node():

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def merge(t1, t2):
    if not t1:
        return t2
    if not t2:
        return t1
    t1.val = t1.val + t2.val
    t1.left = merge(t1.left, t2.left)
    t2.right = merge(t1.right, t2.right)
    return t1


