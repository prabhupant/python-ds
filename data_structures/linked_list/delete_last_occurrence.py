class Node():

    def __init__(self, val):
        self.val = val
        self.next = None

def delete_last_occurrence(head, val):
    if not head:
        return None

    curr = head
    prev = None
    final_prev = None
    final_occ = None

    while curr != None:
        if curr.val == val:
            final_prev = prev
            final_occ = curr
        
        prev = curr
        curr = curr.next

    
    if final_occ:
        # special case that checks for a 1 node list that equals the val
        if final_prev:
            final_prev.next = final_occ.next
        else:
            head = None
    
    return head