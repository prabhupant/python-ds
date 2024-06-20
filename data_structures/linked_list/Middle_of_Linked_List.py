# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        temp = head
        count = 0
        while(temp!=None):
            count+=1
            temp=temp.next
        count=int(count/2)
        i=0
        while(i!=count):
            head=head.next
            i+=1
        return(head)
