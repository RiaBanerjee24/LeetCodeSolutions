'''
Difficulty: Medium

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return
        queue = []
        all_lvl = []
        head = root
        queue.append(head)
        while queue:           
            level = []
            lvl_size = len(queue)
            for _ in range(lvl_size):
                node = queue.pop(0)
                level.append(node)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            all_lvl.append(level)
        print(all_lvl)

        for level in all_lvl:
            for i in range(len(level)):                
                if (i+1)>=len(level):
                    level[i].next = None
                else:                    
                    level[i].next = level[i+1]
        
        
        return root
