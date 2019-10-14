# Python program to find the node with minimum value in bst 
  
# A binary tree node 
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, key): 
        self.data = key 
        self.left = None
        self.right = None
  
""" Give a binary search tree and a number,  
inserts a new node with the given number in  
the correct place in the tree. Returns the new  
root pointer which the caller should then use  
(the standard trick to avoid using reference  
parameters). """
def insert(node, data): 
  
    # 1. If the tree is empty, return a new, 
    # single node 
    if node is None: 
        return (Node(data)) 
  
    else: 
        # 2. Otherwise, recur down the tree 
        if data <= node.data: 
            node.left = insert(node.left, data) 
        else: 
            node.right = insert(node.right, data) 
  
        # Return the (unchanged) node pointer 
        return node 
  
""" Given a non-empty binary search tree,   
return the minimum data value found in that  
tree. Note that the entire tree does not need  
to be searched. """
def minValue(node): 
    current = node 
  
    # loop down to find the lefmost leaf 
    while(current.left is not None): 
        current = current.left 
  
    return current.data 
  
# Driver program 
root = None
root = insert(root,4) 
insert(root,2) 
insert(root,1) 
insert(root,3) 
insert(root,6) 
insert(root,5) 
  
print "\nMinimum value in BST is %d"  %(minValue(root)) 
