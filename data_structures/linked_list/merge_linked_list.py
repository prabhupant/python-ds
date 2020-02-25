class Node():

    def __init__(self, val):
        self.val = val
        self.next = None


def merge(l1, l2):
    if not l1 and not l2:
        return
    elif not l2:
        return l1
    elif not l1:
        return l2

    if (l1.val < l2.val):
        l1.next = merge(l1.next, l2)
        return l1
    l2.next = merge(l1, l2.next)
    return l2

head1 = Node(1)
head1.next = Node(3)

head2 = Node(2)
head2.next = Node(4)

head_merged = merge(head1,head2)

ptr = head_merged
while ptr:
    print(ptr.val)
    ptr = ptr.next

