'''
Author : MiKueen
Level : Easy
Problem Statement : Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # BFS solution
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        
        depth, level = 1, deque([root])
        while level:
            for i in range(len(level)):
                node = level.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            depth += 1      
        return depth
    