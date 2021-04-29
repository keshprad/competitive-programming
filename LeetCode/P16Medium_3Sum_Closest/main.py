from typing import List
# Problem: https://leetcode.com/problems/3sum-closest/


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closest = sum(nums[:3])
        for i in range(len(nums)-2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = sum((nums[i], nums[l], nums[r]))
                if abs(s-target) < abs(closest-target):
                    closest = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return target
        return closest
