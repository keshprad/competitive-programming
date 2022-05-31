from typing import List
# Problem: https://leetcode.com/problems/missing-number/


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''O(n) runtime, O(1) space solution using XOR

        In order to understand this solution, these key properties of XOR
        should be known.
        a ^ a = 0
        a ^ 0 = a
        a ^ b = b ^ a

        Using these properties we see that XOR'ing the list of nums with all
        the nums from 0 to n, will allow all matching a's to XOR with each
        other (a ^ a = 0). This would leave 0 ^ (the last num, which doesn't
        exist in nums). This will equal itself.
        '''
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
