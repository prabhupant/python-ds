class Node():

    def __init__(self, val):
        self.val = val
        self.next = None

def delete(head, val):
    if head == None:
        return "List is empty"
    
    curr = head
    prev = None

    while curr.val != val:
        if curr.next == head:
            return "Val not in list"
        prev = curr
        curr = curr.next

    if curr.next == head:
        head = None
        return "Deleted"

    if curr == head:
        prev = head
        while prev.next != head:
            prev = prev.next
        head = curr.next
        prev.next = head

    elif curr.next == head:
        prev.next = head

    else:
        prev.next = curr.next

    return "Deleted"
        
