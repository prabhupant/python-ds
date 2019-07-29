class Node():

    def __init__(self, val):
        self.val = val
        self.next = None

def reverse(head):
    if not head:
        return None
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

curr = head
while curr:
    print(curr.val)
    curr = curr.next

new_head = reverse(head)
curr = new_head
while curr:
    print(curr.val)
    curr = curr.next



