# Problem: https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        '''This solution will only loop once for each 1'''
        ones = 0
        while (n != 0):
            # this skips all 0s until the next 1
            n &= n - 1
            ones += 1
        return ones

    def hammingWeight2(self, n: int) -> int:
        '''This solution will loop for every 0 between the 1s'''
        ones = 0
        while (n != 0):
            ones += n & 1
            n >>= 1
        return ones
