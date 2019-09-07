class Node():

    def __init__(self, val):
        self.val = val
        self.next = None


def pair_swap(head):
    if head == None or head.next == None:
        return head
    root = head.next
    curr = head
    prev = Node(0)

    while curr.next:
        curr.next = curr.next.next
        curr.next.next = curr
        prev.next = curr.next.next
        prev = curr.next
        curr = curr.next.next
    return root


