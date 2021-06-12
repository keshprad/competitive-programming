from typing import List
from itertools import accumulate
# Problem: https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        accumulated = list(accumulate(nums))
        end = len(nums) - 1
        splits, j, k = 0, 0, 0
        for i in range(len(nums) - 2):
            while j <= i or (j < end and accumulated[j] < 2*accumulated[i]):
                j += 1
            while k < j or (k < end and accumulated[k] - accumulated[i] <= accumulated[end] - accumulated[k]):
                k += 1
            splits += k - j
        return splits % (1e9+7)
