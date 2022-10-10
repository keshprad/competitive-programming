from typing import List
# Problem: https://leetcode.com/problems/koko-eating-bananas/


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eating_hours(piles: List[int], k: int) -> int:
            h = 0

            for p in piles:
                # (p // k) is num hours to eat p bananas if p is divisible by k
                # (p % k != 0) adds 1 more hour if there are bananas remaining
                h += (p // k) + (p % k != 0)
            return h

        l = 1
        r = max(piles)

        while l <= r:
            k = l + (r - l) // 2
            hrs = eating_hours(piles, k)

            if hrs > h:
                # koko not eating fast enough
                l = k + 1
            else:
                # valid k value, check if koko can eat slower
                r = k - 1
        return l
