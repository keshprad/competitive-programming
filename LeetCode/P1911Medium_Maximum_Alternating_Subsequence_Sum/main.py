from typing import List
# Problem: https://leetcode.com/problems/maximum-alternating-subsequence-sum/description/


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}
        dp[(len(nums), 1)] = 0
        dp[(len(nums), -1)] = 0

        def maxAltSum(i, sign):
            if (i, sign) in dp:
                # cache hit
                return dp[(i, sign)]

            # choose between consuming character or proceeding to next
            dp[(i, sign)] = max(sign*nums[i] + maxAltSum(i+1, -sign),
                                maxAltSum(i+1, sign))
            return dp[(i, sign)]

        return maxAltSum(0, 1)
