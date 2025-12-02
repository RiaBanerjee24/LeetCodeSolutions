'''
Difficulty: Medium
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def expand(left,right):
            while left>=0 and right<n and s[left]==s[right]:
                left -=1
                right +=1
            return right,left+1
        max_sub = ""
        max_len = 0
        for i in range(n):
            r1,l1 = expand(i,i)
            r2,l2 = expand(i,i+1)
            s1 = s[l1:r1]
            s2 = s[l2:r2]
            sn1 = len(s1)
            sn2 = len(s2)
            if sn1>=sn2 and sn1>max_len:
                max_sub = s1
                max_len = sn1
            elif sn2>sn1 and sn2>max_len:
                max_sub = s2
                max_len = sn2
        return max_sub