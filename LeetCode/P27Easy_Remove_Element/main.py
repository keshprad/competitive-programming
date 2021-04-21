from typing import List
# Problem: https://leetcode.com/problems/remove-element/


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums[i:] = nums[i+1:]
            else:
                i += 1
        return len(nums)
