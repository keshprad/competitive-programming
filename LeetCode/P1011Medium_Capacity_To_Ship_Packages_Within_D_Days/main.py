from typing import List
# Problem: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # lower and upper bounds for least capacity
        l_cap, u_cap = max(weights), sum(weights)

        # Now this is a binary search problem
        # Search for the least capacity between the bounds
        while l_cap < u_cap:
            mid_cap = (l_cap + u_cap) // 2

            # Check if possible to ship packages with the mid_cap
            if self.can_ship_at_cap(weights, days, mid_cap):
                # If yes, reduce the upper bound and continue search
                u_cap = mid_cap
            else:
                # Otherwise, increase the lower bound and continue search
                l_cap = mid_cap + 1
        return l_cap

    def can_ship_at_cap(self, weights: List[int], days: int, cap: int) -> bool:
        num_days = 0
        curr_weight = 0

        for w in weights:
            if curr_weight + w <= cap:
                curr_weight += w
            else:
                num_days += 1
                curr_weight = w

        return num_days + 1 <= days
