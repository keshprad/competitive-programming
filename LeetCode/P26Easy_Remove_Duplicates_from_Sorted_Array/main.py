from collections import OrderedDict
from typing import List
# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates_1(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)

    def removeDuplicates_2(self, nums: List[int]) -> int:
        nums[:] = OrderedDict.fromkeys(nums)
        return len(nums)

    def removeDuplicates_3(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        while i < len(nums):
            if i > 0 and nums[i-1] == nums[i]:
                nums[i:] = nums[i+1:]
            else:
                i += 1
        return len(nums)
