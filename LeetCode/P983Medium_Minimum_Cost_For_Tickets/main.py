from typing import List
# Problem: https://leetcode.com/problems/minimum-cost-for-tickets/


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # start cost of every day travel at infinity
        dp = [float('inf')] * (days[-1]+1)
        # base case, day 0 costs 0
        dp[0] = 0
        # convert to set
        days = set(days)

        for i in range(1, len(dp)):
            if i in days:
                # traveling today, try every ticket type
                for cost, k in zip(costs, (1, 7, 30)):
                    # 3 options:
                    # 1. current option
                    # 2. buying ticket covering last k days
                    # 3. buy ticket covering more days than currently traveled (use i - min(i, k))
                    dp[i] = min(dp[i], cost + dp[i-min(i, k)])
            else:
                # not traveling, don't purchase tickets
                dp[i] = dp[i-1]
        return dp[-1]
