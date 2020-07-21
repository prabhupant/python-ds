class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


def detect_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next

    return True


# TESTING
if __name__ == "__main__":
    HEAD = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    HEAD.next = second
    second.next = third
    third.next = fourth

    print(detect_cycle(HEAD))
