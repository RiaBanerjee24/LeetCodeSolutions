'''
Difficulty: Medium

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        path =[]
        path.append(root)
        queue = []
        queue.append(root)
        all_path = []
        while queue:
            lvl_size = len(queue)          
            level = []
            for _ in range(lvl_size):
                node = queue.pop(0)
                
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            all_path.append(level)
        print(all_path)
        return all_path
