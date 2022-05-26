from typing import List
# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # l repr the buy day
        # r repr the sell day
        l, r = 0, 1

        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            if curr_profit > 0:
                # positive profit. Update max profit
                profit = max(profit, curr_profit)
            else:
                # negative profit means the curr sell day is lower
                # this will be the new buy day
                # new buy day has lower price (more optimal)
                l = r
            r += 1
        return profit
