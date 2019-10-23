'''
Author : MiKueen
Level : Medium
Problem Statement : Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.
For example, given the following tree:
    1
   / \
  2   5
 / \   \
3   4   6

The flattened tree should look like:
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

Approach : Recursive solution
1. Flatten left subtree
2. Find tail of left subtree
3. Attach tail of left subtree to starting node of right subtree
4. Flatten right subtree
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return
        
        right = root.right
        if root.left:
            self.flatten(root.left)
            tail = root.left
            while tail.right:
                tail = tail.right
            root.left, root.right, tail.right = None, root.left, right
        self.flatten(right)
                    