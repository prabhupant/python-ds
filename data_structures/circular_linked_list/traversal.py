class Node():

    def __init__(self, val):
        self.val = val
        self.next = None

def push(head, val):
    if not head:
        head = Node(val)
        head.next = head
        return
    curr = head
    while curr:
        if curr.next == head:
            break
        curr = curr.next
    curr.next = Node(val)
    curr.next.next = head


def print_list(head):
    if not head:
        return
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
        if curr == head:
            break

first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third
third.next = first

print_list(first)

push(first, 4)

print_list(first)
