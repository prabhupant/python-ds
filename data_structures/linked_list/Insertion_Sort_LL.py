class Node():

    def __init__(self, val):
        self.val = val
        self.next = None



def revert(node):
    ''' Revert list in-place '''

    prev = None
    while node:
        prev, node.next, node = node, prev, node.next

    return prev


class Solution:
	# A : head node of linked list
	# return the head node in the linked list
	def insertionSortList(self, A):

	    source = A
	    dest = None

	    while source:
	        prev = None
	        node = dest
	        # Find insertion point (between prev and node)
	        while node and node.val > source.val:
	            prev, node = node, node.next
	        if prev is None:
	            dest = source
	        else:
	            prev.next = source
	        source.next, source = node, source.next

	    return revert(dest)