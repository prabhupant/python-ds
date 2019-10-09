class Node:
	def __init__(self,data):
		self.data=data
		self.left=self.right=None
class tree:
	def __init__(self):
		self.head=None
	def inorder(self,head):
		if(head):
			self.inorder(head.left)
			print(head.data,end=" ")
			self.inorder(head.right)
	def checkidentical(self,head1,head2):
		if(not head1 and not head2):
			return	True
		if head1 and head2:
			return (head1.data==head2.data) and self.checkidentical(head1.left,head2.left) and self.checkidentical(head1.right,head2.right)
		return False
	def getmirror(self,head):
		if not head:
			return
		self.getmirror(head.left)
		self.getmirror(head.right)
		head.left,head.right=head.right,head.left
if __name__ =="__main__":  
	root = Node(1)  
	root.left = Node(2)  
	root.right =Node(3)  
	root.left.left =Node(4)  
	root.left.right =Node(5) 
	root1 = Node(1)  
	root1.left = Node(2)  
	root1.right =Node(3)  
	obj=tree()
	obj.inorder(root)
	obj.getmirror(root)
	obj.inorder(root)
