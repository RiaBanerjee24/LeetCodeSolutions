'''
Difficulty: Medium
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_cnt = 0

        def dfs(node,maxval):
            if not node:
                return 
            
            if node.val>=maxval:
                self.good_cnt +=1
            maxval = max(maxval,node.val)
            dfs(node.left,maxval)
            dfs(node.right,maxval)
        dfs(root,root.val)
        return self.good_cnt