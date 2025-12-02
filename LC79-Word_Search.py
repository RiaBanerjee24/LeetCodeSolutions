'''
Difficulty: Medium
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
'''

from typing import List
class Solution:    
    def exist(self, board: List[List[str]], word: str) -> bool:
        word = list(word)
        m = len(board)
        n = len(board[0])
        l=len(word)
        
        def dfs(r,c,i,visited):
            if i==l:
                return True
            if r<0 or r>=m or c<0 or c>=n or (r,c) in visited or board[r][c]!=word[i]:
                return False
            visited.add((r,c))
            res = dfs(r-1,c,i+1,visited) or dfs(r+1,c,i+1,visited) or dfs(r,c-1,i+1,visited) or dfs(r,c+1,i+1,visited)
            visited.remove((r,c))
            return res
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if dfs(i,j,0,set()):
                        return True
        return False