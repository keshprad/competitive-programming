from typing import List
# Problem: https://leetcode.com/problems/house-robber-ii/


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(nums: List[int]) -> int:
            r1, r2 = 0, 0

            for n in nums:
                r1, r2 = r2, max(r1+n, r2)
            return r2
        return max(nums[0], rob(nums[1:]), rob(nums[:-1]))
