'''
Difficulty: Medium
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordmap = defaultdict(list)
        for i in range(len(strs)):
            s_sorted = ''.join(str(sorted(strs[i])))
            if s_sorted in wordmap:
                wordmap[s_sorted].append(i)
            else:
                wordmap[s_sorted] = [i]
        groups = []
        for _,idxes in wordmap.items():
            group = []
            for idx in idxes:
                group.append(strs[idx])
            groups.append(group)
        return groups
