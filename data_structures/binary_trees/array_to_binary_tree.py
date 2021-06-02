"""
Convert an array to a binary tree

Sample input - 
[1,2,3,4,5,null,6,7,null,null,null,null,8]

Note - 
if a tree has N nodes and is complete, then the no of internal
nodes can be (N-1) / 2
"""

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create_tree(arr):
    curr_ptr = 0
    child_ptr = 0

    root = Node(arr[0])
    curr_node = root

    while i < (len(arr) - 1)/2:
        curr_ptr = arr[i]
        child_ptr = i + 1

        left_child = arr[child_ptr]
        right_child = arr[child_ptr + 1]
        
        curr_node.left = Node(left_child)
        curr_node.right = Node(right_child)


