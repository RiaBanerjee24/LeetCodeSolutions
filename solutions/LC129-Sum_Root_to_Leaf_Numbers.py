'''
Difficulty: Medium

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
'''

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:    
    def dfs(self,path,result,root):
        if root is None:
            return
        path.append(str(root.val))
        if root.right is None and root.left is None:
            result.append("".join(list(path)))
        self.dfs(path,result,root.left)
        self.dfs(path,result,root.right)
        path.pop()
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []
        self.dfs([],result,root)
        res = 0
        for e in result:
            i = int(e)
            res += i       
        return res