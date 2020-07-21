class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def push(head, data):
    node = Node(data)
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = node


def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=' ')
        curr = curr.next


def sum_numbers(head1, head2):
    temp = None
    carry = 0
    prev = None
    res = None
    while head1 is not None or head2 is not None:
        data1 = 0 if head1 is None else head1.val
        data2 = 0 if head2 is None else head2.val
        s = carry + data1 + data2
        carry = 1 if s >= 10 else 0
        s = s if s < 10 else s % 10

        temp = Node(s)

        # if this is the first node, make it head
        if res is None:
            res = temp
        else:
            prev.next = temp

        prev = temp

        # move pointers ahead
        if head1 is not None:
            head1 = head1.next
        if head2 is not None:
            head2 = head2.next

    if carry > 0:
        temp.next = Node(carry)

    return res


# TESTING
if __name__ == "__main__":
    HEAD1 = Node(1)
    push(HEAD1, 2)
    push(HEAD1, 3)
    push(HEAD1, 4)
    print_list(HEAD1)
    print()
    HEAD2 = Node(5)
    push(HEAD2, 2)
    push(HEAD2, 1)
    push(HEAD2, 3)
    print_list(HEAD2)
    print()
    summmed_list = sum_numbers(HEAD1, HEAD2)
    print_list(summmed_list)
