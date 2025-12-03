'''
Difficulty: Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
'''
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        all_prod = 1
        result = [0]*len(nums)
        zero_cnt = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                all_prod *=nums[i]
            else:
                zero_cnt +=1
        if zero_cnt>1:
            return result
        for i in range(len(nums)):
            if zero_cnt==1 and nums[i]==0:
                result[i] = all_prod
            elif zero_cnt==1 and nums[i]!=0:
                result[i]=0
            elif zero_cnt==0:
                result[i]=int(all_prod/nums[i])
        return result
        