# -*- coding: utf-8 -*-
'''
 Program to implement binary tree using binary tree
 left node of tree will be stored at (root index * 2) + 1
 while right node will be stored at  (root index * 2) + 2
'''

def fill_root(val):
    if(tree_ary[0] != None):
        print("Cant set root")
    else:
        tree_ary[0] = val
    return True    

def add_to_left(val,parent):
    if(tree_ary[parent] == None):
        print("Cant set child")
    else:
        tree_ary[(parent * 2) + 1] = val
        print("Added "+ str(val))
        

def add_to_right(val,parent):
    if(tree_ary[parent] == None):
        print("Cant set child")
    else:
        tree_ary[(parent * 2) + 2] = val
        print("Added " + str(val))
   


def view_tree():        # Function to print tree in BFS manner
    for node in tree_ary:
        if(node != None):
            print(str(node))
            

def find_height():
    ind = -1
    po = 0
    for itr in range(0,len(tree_ary)):
            if(tree_ary[itr] != None):
                ind = itr
    if(ind == -1):
        return 0
    while True:
       if(2 ** po > ind):
           return po - 1
       po += 1

if __name__ == "__main__":
    
    tree_ary = [None] * 100  
    fill_root(5)
    add_to_left(2,0)
    add_to_right(3,0)
    add_to_left(7,1)
    view_tree()
    print("Height is ",find_height())
     

    
    
    
