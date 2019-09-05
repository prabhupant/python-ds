class Node():

    def __init__(self, val):
        self.val = val
        self.next = None


def remove(head, n):
    res = head
    slow = head
    fast = head

    for i in range(n+1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return res

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print_list(head)
remove(head, 2)
print_list(head)


