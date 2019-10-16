
### Node definition that is used


#class Node:
#    def __init__(self, val):
#        self.val = val
#        self.leftChild = None
#        self.rightChild = None

def find(self, val):
    return self.findNode(self.root, val)

def findNode(self, currentNode, val):
    if(currentNode is None):
        return False
    elif(val == currentNode.val):
        return True
    elif(val < currentNode.val):
        return self.findNode(currentNode.leftChild, val)
    else:
        return self.findNode(currentNode.rightChild, val)
