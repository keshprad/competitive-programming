from typing import List
# Problem: https://leetcode.com/problems/minimum-size-subarray-sum/


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sub_sum = 0
        min_len = float('inf')

        for i, num in enumerate(nums):
            sub_sum += num
            while sub_sum >= target:
                min_len = min(min_len, i + 1 - l)
                sub_sum -= nums[l]
                l += 1

        return min_len if min_len != float('inf') else 0
