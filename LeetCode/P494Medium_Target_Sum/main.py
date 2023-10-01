from typing import List
# Problem: https://leetcode.com/problems/target-sum/


class Solution:
    def __init__(self):
        self.memo = {}

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.dp(nums, target, len(nums) - 1, 0)

    def dp(self, nums, target, idx, curr_sum):
        if (idx, curr_sum) in self.memo:
            # base case (memoization)
            return self.memo[(idx, curr_sum)]

        # reached base case
        if idx < 0:
            # return 1 if successful base case, 0 oteherwise
            return curr_sum == target

        pos = self.dp(nums, target, idx-1, curr_sum + nums[idx])
        neg = self.dp(nums, target, idx-1, curr_sum - nums[idx])

        self.memo[(idx, curr_sum)] = pos + neg
        return pos + neg
