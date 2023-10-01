from typing import List
# Problem: https://leetcode.com/problems/partition-equal-subset-sum/


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        # set up dp matrix
        dp = [[False]*(target+1) for _ in range(len(nums)+1)]
        dp[0][0] = True

        for i in range(1, len(nums)+1):
            num = nums[i-1]
            for j in range(target+1):
                dp[i][j] = dp[i-1][j] or (num <= j and dp[i-1][j-num])
        return dp[-1][-1]
