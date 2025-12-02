'''
Difficulty: Easy

You are given a 2D matrix grid of size m x n. You need to check if each cell grid[i][j] is:

Equal to the cell below it, i.e. grid[i][j] == grid[i + 1][j] (if it exists).
Different from the cell to its right, i.e. grid[i][j] != grid[i][j + 1] (if it exists).
Return true if all the cells satisfy these conditions, otherwise, return false.

 

Example 1:

Input: grid = [[1,0,2],[1,0,2]]

Output: true

Example 2:

Input: grid = [[1,1,1],[0,0,0]]

Output: false

Constraints:

1 <= n, m <= 10
0 <= grid[i][j] <= 9
'''
from typing import List
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid)):
            col = []
            for j in range(len(grid[0])):
                if len(col)>0 and grid[i][j-1]==grid[i][j]:
                    return False
                col.append(grid[i][j])
                print(col)
        for j in range(len(grid[0])):
            row = []
            for i in range(len(grid)):
                if len(row)>0 and grid[i][j] not in row:
                    return False
                row.append(grid[i][j])
        return True

