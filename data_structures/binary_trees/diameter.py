class Node: 
    def __init__(self, data):  
        self.data = data  
        self.left = self.right = None
def height(root,diameter):
	if root==None:
		return 0
	leftheight=height(root.left,diameter)
	rightheight=height(root.right,diameter)
	diameter[0]=max(diameter[0],1+leftheight+rightheight)
	return 1+max(leftheight,rightheight)
def getlevel(root,k,level):
	if root==None:
		return -1
	if root.data==k:
		return level
	level1=getlevel(root.left,k,level+1)
	if level1!=-1:
		return level1
	level2=getlevel(root.right,k,level+1)
	if level2!=-1:
		return level2
	return -1
def kdistance(root,k):
	if root==None or k<0:
		return
	if k==0:
		print(root.data)
		return
	kdistance(root.left,k-1)
	kdistance(root.right,k-1)
def kdistancenode(root,target,k):
	if root==None:
		return -1
	if root==target:
		kdistance(root,k)
		return 0
	ld=kdistancenode(root.left,target,k)
	if ld!=-1:
		if ld+1==k:
			print(root.data)
		else:
			kdistance(root.right,k-ld-2)
		return ld+1
	rd=kdistancenode(root.right,target,k)
	if rd!=-1:
		if rd+1==k:
			print(root.data)
		else:
			kdistance(root.left,k-rd-2)
		return rd+1
	return -1
if __name__ == '__main__': 
	root = Node(20) 
	root.left = Node(8) 
	root.right = Node(22) 
	root.left.left = Node(4) 
	root.left.right = Node(12) 
	root.left.right.left = Node(10) 
	root.left.right.right = Node(14) 
	target = root.left.right
	kdistancenode(root,target,2) 
