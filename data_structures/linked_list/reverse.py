class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


def reverse(head):
    if not head:
        return None
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


# TESTING
if __name__ == "__main__":
    HEAD = Node(1)
    HEAD.next = Node(2)
    HEAD.next.next = Node(3)

    CURR = HEAD
    while CURR:
        print(CURR.val)
        CURR = CURR.next

    new_head = reverse(HEAD)
    CURR = new_head
    while CURR:
        print(CURR.val)
        CURR = CURR.next
