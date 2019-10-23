class Node:

    def __init__(self, x):
        self.val = x
        self.next = None

        
def merge_two_lists(l1, l2):
    if not l1 and not l2:
        return
    elif not l2:
        return l1
    elif not l1:
        return l2

    if (l1.val < l2.val):
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    l2.next = merge_two_lists(l1, l2.next)
    return l2


def merge_k_lists(lists):
    length = len(lists)
    if length == 0:
        return;
    elif length == 1:
        return lists[0]
    elif length == 2:
        return merge_two_lists(lists[0], lists[1])

    mid = length // 2

    left_half = lists[:mid]
    right_half = lists[mid:]

    return merge_two_lists(merge_k_lists(left_half), merge_k_lists(right_half))
