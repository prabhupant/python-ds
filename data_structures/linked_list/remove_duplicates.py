class Node():

    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return "{}".format(self.val)


def remove_duplicates(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    while head and head.next:
        if head.val == head.next.val:
            temp = head
            while temp.next and temp.next.val == temp.val:
                temp = temp.next
            prev.next = temp.next
            head = temp.next
        else:
            head = head.next
            prev = prev.next
    return dummy.next
