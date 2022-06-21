from typing import List
# Problem: https://leetcode.com/problems/single-number-ii/


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        # iterate each bit
        for i in range(32):
            count = 0

            # for every num, check count 1 bits at this spot
            for num in nums:
                if num & (1 << i):
                    count += 1
            # mod 3 because we only want the one that doesn't occur 3 times
            res |= (count % 3) << i

        return res if res < (1 << 31) else res - (1 << 32)
