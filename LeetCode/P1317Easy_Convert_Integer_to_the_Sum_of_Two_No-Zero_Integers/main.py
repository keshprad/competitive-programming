# Problem: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for k in range(n):
            if '0' not in f'{k}{n-k}':
                return [k, n-k]
