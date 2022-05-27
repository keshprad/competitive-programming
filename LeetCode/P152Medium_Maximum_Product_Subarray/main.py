from typing import List
# Problem: https://leetcode.com/problems/maximum-product-subarray/


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_rev = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            nums_rev[i] *= nums_rev[i-1] or 1

        return max(max(nums), max(nums_rev))
