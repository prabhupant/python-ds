# Number at odd places should come first 
# followed by even places numbers

class Node():

    def __init__(self, val):
        self.val = val
        self.next = None


def arrange(head):
    if not head:
        return None
    odd = head
    even = head.next
    even_head = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head

