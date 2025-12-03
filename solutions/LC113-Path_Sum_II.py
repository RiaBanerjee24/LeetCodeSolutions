'''
Difficulty: Medium

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
'''
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def __init__(self):
        self.cnt = 0
    def dfs(self,path,result,root,target):
        self.cnt += 1        
        if root is None:           
            return       
        path.append(root.val)
        if root.left is None and root.right is None:
            if root.val == target:
                result.append(list(path))
        self.dfs(path,result,root.left,target-root.val)
        self.dfs(path,result,root.right,target-root.val)        
        path.pop()
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []        
        self.dfs([],result,root,targetSum)        
        return result