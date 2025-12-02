'''
Difficulty: Medium
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnt = Counter(s1)        
        left = 0
        right = len(s1)-1

        while right<len(s2):
            sub = s2[left:right+1]
            s2_cnt = Counter(sub)
            if s1_cnt==s2_cnt:
                return True
            right +=1
            left +=1
        return False