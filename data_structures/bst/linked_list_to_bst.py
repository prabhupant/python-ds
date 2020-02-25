class TreeNode():

    def __init__(self, val ,left, right):
        self.val = val
        self.left = None
        self.right = None


class LLNode():

    def __init__(self, val, next):
        self.val = val
        self.next = None


def linked_list_to_bst(head):
    if not head:
        return None
    curr = head
    n = 0
    while curr:
        n += 1
        curr = curr.next

    return ll_to_bst_recur(head, n)


def ll_to_bst_recur(head, n):
    if n <= 0:
        return None
    # TODO: Fix me!
    # left = ll_to_bst_recur(
    
