from typing import List
# Problem: https://leetcode.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        subs_dp = [0] * n

        # base case
        subs_dp[0] = max_subsum = nums[0]

        # following cases
        for idx in range(1, n):
            if subs_dp[idx-1] <= 0:
                # if starting at a prev idx lowers (or doesn't effect) the sum
                # start at curr num
                subs_dp[idx] = nums[idx]
            else:
                # starting at a prev idx increases the sum
                # start at the best prev idx
                subs_dp[idx] = nums[idx] + subs_dp[idx-1]
            max_subsum = max(max_subsum, subs_dp[idx])
        return max_subsum
