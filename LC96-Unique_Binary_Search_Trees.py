'''
Difficulty: Medium

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.


'''
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
    
    # Base cases
        dp[0] = 1  # There is one empty tree
        dp[1] = 1  # There is one tree with a single node
        
        # Fill the dp array using the recurrence relation
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        
        return dp[n]