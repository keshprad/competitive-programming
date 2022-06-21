from functools import reduce
from operator import xor
from typing import List
# Problem: https://leetcode.com/problems/single-number/


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res

    def singleNumber2(self, nums: List[int]) -> int:
        return reduce(xor, nums)
