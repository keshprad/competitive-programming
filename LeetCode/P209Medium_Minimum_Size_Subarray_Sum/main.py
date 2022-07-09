from typing import List
# Problem: https://leetcode.com/problems/minimum-size-subarray-sum/


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pref = {}
        curr = 0
        min_len = float('inf')

        for i, num in enumerate(nums):
            curr += num
            pref[num] = i

            if curr - target in pref:
                min_len = min(min_len, i - pref[curr - target])

        return min_len if min_len != float('inf') else 0
