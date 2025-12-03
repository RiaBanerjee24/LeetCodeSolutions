'''
Difficulty: Medium
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
'''
from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        all_sum = 0
        n = len(nums)
        for i in range(n):
            all_sum += nums[i]
        
        if all_sum%2!=0:
            return False
        target = all_sum/2
        if target in nums:
            return True
        possible_sums = set()
        possible_sums.add(0)
        for num in nums:
            new_sums = set()
            for s in possible_sums:
                total = s+num
                if total==target:
                    return True
                if total<target:
                    new_sums.add(total)
            possible_sums |=new_sums
        return target in possible_sums 