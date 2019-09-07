class Node():

    def __init__(self, val):
        self.val = val
        self.next = None


def check(head):
    if not head:
        return True
    curr = head
    while curr:
        if curr.next == head:
            return True
        elif curr.next == None:
            return False
        curr = curr.next


first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third

print(check(first))
