class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_spiral(root):

    s1 = []
    s2 = []

    s1.append(root)

    while not len(s1) == 0 or not len(s2) == 0:

        while not len(s1) == 0:
            temp = s1.pop()
            print(temp.data, end=' ')

            if temp.right:
                s2.append(temp.right)
            if temp.left:
                s2.append(temp.left)

        while not len(s2) == 0:
            temp = s2.pop()
            print(temp.data, end=' ')

            if temp.left:
                s1.append(temp.left)
            if temp.right:
                s1.append(temp.right)
