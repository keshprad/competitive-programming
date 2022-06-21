from functools import reduce
from operator import xor
from typing import List
# Problem: https://leetcode.com/problems/single-number-iii/


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # get xor of all nums
        xor_nums = reduce(xor, nums)
        # gets the rightmost non-zero bit
        nzbit = xor_nums & (xor_nums - 1) ^ xor_nums
        # num1 is the xor of all nums with this nzbit
        num1 = reduce(xor, filter(lambda num: num & nzbit, nums))
        # find num2 from the xor of all nums and num1
        num2 = num1 ^ xor_nums
        return num1, num2
