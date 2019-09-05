class Node():

    def __init__(self, val):
        self.val = val
        self.next = None


def merge(l1, l2):
    res = curr = Node(0)
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = 
