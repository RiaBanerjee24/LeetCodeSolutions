'''
Difficulty: Easy
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

'''
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = Counter(s)
        t1 = Counter(t)
        if s1==t1:
            return True
        return False