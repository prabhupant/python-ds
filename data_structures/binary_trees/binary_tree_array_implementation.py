# -*- coding: utf-8 -*-
'''
 Program to implement binary tree using binary tree
 left node of tree will be stored at (root index * 2) + 1
 while right node will be stored at  (root index * 2) + 2
'''

def fillRoot(val):
    if(treeAry[0] != None):
        print("Cant set root")
    else:
        treeAry[0] = val
    return True    

def addToLeft(val,parent):
    if(treeAry[parent] == None):
        print("Cant set child")
    else:
        treeAry[(parent * 2) + 1] = val
        print("Added "+ str(val))
        

def addToRight(val,parent):
    if(treeAry[parent] == None):
        print("Cant set child")
    else:
        treeAry[(parent *2 ) + 2] = val
        print("Added " + str(val))
   

# Function to print tree in BFS manner
def viewTree():
    for node in treeAry:
        if(node != None):
            print(str(node))
            

def findHeight():
    ind = -1
    po = 0
    for itr in range(0,len(treeAry)):
            if(treeAry[itr] != None):
                ind = itr
    if(ind == -1):
        return 0
    while True:
       if(2 ** po > ind):
           return po - 1
       po += 1

if __name__=="__main__":
    
    treeAry = [None] * 100  
    fillRoot(5)
    addToLeft(2,0)
    addToRight(3,0)
    addToLeft(7,1)
    # finding height of the tree
    treeHeight = findHeight()
     

    
    
    
