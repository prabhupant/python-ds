class Node:
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


# TESTING
if __name__ == "__main__":
    HEAD = Node(1)
    HEAD.next = Node(2)
    HEAD.next.next = Node(3)
    HEAD.next.next.next = Node(4)
    HEAD.next.next.next.next = Node(5)
    print_list(HEAD)
    remove(HEAD, 2)
    print_list(HEAD)
