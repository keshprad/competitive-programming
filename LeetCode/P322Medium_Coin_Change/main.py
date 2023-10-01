from typing import List
# Problem: https://leetcode.com/problems/coin-change/


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}
        for i in range(len(coins)-1, -1, -1):
            coin = coins[i]
            for j in range(1, amount+1):
                dp[j] = min(dp.get(j, float('inf')),
                            1 + dp.get(j - coin, float('inf')))
        return -1 if dp[amount] == float('inf') else dp[amount]
