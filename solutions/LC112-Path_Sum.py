'''
Difficulty: Easy

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''

from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            if targetSum==root.val:
                return True
        res = self.hasPathSum(root.left,targetSum-root.val)
        res2 = self.hasPathSum(root.right,targetSum-root.val)
        if res or res2:
            return True
        return False
        