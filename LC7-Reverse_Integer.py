'''
Difficulty: Medium
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
'''

class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        neg = False
        if x<0:
            neg = True
        x = abs(x)
        i=1
        j = 0
        ans = ''
        while x>0:            
            rem = x%pow(10,i)
            x = x-rem
            rem = rem/pow(10,j)
            ans += str(int(rem))
            print(rem)
            i+=1
            j+=1
        ans = int(ans)
        if ans>(pow(2,31)-1) or ans<-pow(2,31):
            return 0
        if neg:
            return -ans
        return ans
