from typing import List
# Problem: https://leetcode.com/problems/missing-number/


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''O(n) runtime, O(1) space solution using XOR'''
        # a ^ a = 0
        # a ^ 0 = a
        # a ^ b = b ^ a
        res = 0

        for i, num in enumerate(nums):
            res ^= i
            res ^= num
        res ^= len(nums)

        return res

    def missingNumber2(self, nums: List[int]) -> int:
        '''O(n) runtime, O(1) space solution using gausian sum'''
        n = len(nums)
        tot = (n + 1) * n // 2

        for num in nums:
            tot -= num

        return tot

    def missingNumber3(self, nums: List[int]) -> int:
        '''O(n) runtime, O(1) space solution using sum (preventing overflow)'''
        res = 0

        for i, num in enumerate(nums):
            res += i
            res -= num
        res += len(nums)

        return res
