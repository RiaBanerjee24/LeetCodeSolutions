'''
Difficulty: Medium

You are given an array nums of length n. You are also given an integer k.

You perform the following operation on nums once:

Select a subarray nums[i..j] where 0 <= i <= j <= n - 1.
Select an integer x and add x to all the elements in nums[i..j].
Find the maximum frequency of the value k after the operation.

 

Example 1:

Input: nums = [1,2,3,4,5,6], k = 1

Output: 2

Explanation:

After adding -5 to nums[2..5], 1 has a frequency of 2 in [1, 2, -2, -1, 0, 1].

Example 2:

Input: nums = [10,2,3,4,5,5,4,3,2,2], k = 10

Output: 4

Explanation:

After adding 8 to nums[1..9], 10 has a frequency of 4 in [10, 10, 11, 12, 13, 13, 12, 11, 10, 10].

 

Constraints:

1 <= n == nums.length <= 105
1 <= nums[i] <= 50
1 <= k <= 50

'''

from functools import cache
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        kCount = sum([1 if num == k else 0 for num in nums])
        ans = 0
        def subArraySum(arr):
            @cache
            def best(index, started):
                if index >= len(arr):
                    return 0
                if started:
                    return max(0, arr[index] + best(index + 1, True))
                else:
                    return max(arr[index] + best(index + 1, True), best(index + 1, False))
            return best(0, False)
        
        for i in range(1, 51):
            arr = []
            currI = 0
            if i == k:
                continue
            for num in nums:
                if num == i:
                    if currI < 0:
                        arr.append(currI)
                        currI = 0
                    currI += 1
                elif num == k:
                    if currI > 0:
                        arr.append(currI)
                        currI = 0
                    currI -= 1
            if currI != 0:
                arr.append(currI)

            maxNet = subArraySum(arr)
            # print(i, maxNet, kCount)
            ans = max(ans, kCount + maxNet)
        return ans        

