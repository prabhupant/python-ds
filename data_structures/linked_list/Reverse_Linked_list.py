# Simple and tail recursive Python program to reverse a linked list  
# by yash872
  
# Node class  
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
  
    def reverseUtil(self, curr, prev): 
          
        # If last node mark it head 
        if curr.next is None : 
            self.head = curr  
              
            # Update next to prev node 
            curr.next = prev 
            return 
          
        # Save curr.next node for recursive call 
        next = curr.next
  
        # And update next  
        curr.next = prev 
      
        self.reverseUtil(next, curr)  
  
  
    # This function mainly calls reverseUtil() 
    # with previous as None 
    def reverse(self): 
        if self.head is None: 
            return 
        self.reverseUtil(self.head, None) 
  
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print temp.data, 
            temp = temp.next
  
  
# Driver program 
llist = LinkedList() 
llist.push(8) 
llist.push(7) 
llist.push(6) 
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2) 
llist.push(1) 
  
print "Given linked list"
llist.printList() 
  
llist.reverse() 
  
print "\nReverse linked list"
llist.printList() 
