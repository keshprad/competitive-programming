# Problem: https://leetcode.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case
        if n < 2:
            return n
        # Set up DP array
        dp = [1] * n
        dp[1] = 2

        # DP method to get ways to climb stairs
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
