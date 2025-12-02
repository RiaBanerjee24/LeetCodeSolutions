'''
Difficulty: Medium

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
li = []
class Solution:
    def inorder(self, root:Optional[TreeNode],path) -> List:
        if root is None:
            return
        self.inorder(root.left, path)
        path.append(root.val)
        self.inorder(root.right, path)
        return path
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        path = self.inorder(root,[])
        path_asc = sorted(path)
        # print(path_asc)
        # print(list(set(path_asc)))
        # print(path)
        if path == path_asc and path == sorted(list(set(path_asc))):
            return True
        return False