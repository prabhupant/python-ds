class Node():

    def __init__(self, val):
        self.val = val
        self.next = None


def remove(head, val):
    while head and head.val == val:
        head = head.next
    if not head:
        return None
    curr = head
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
    
