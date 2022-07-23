# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        shift = 0

        for k in range(2, len(nums)):
            # shift element to account for duplicates
            nums[k - shift] = nums[k]

            if nums[k] == nums[i]:
                # track the number of times we have found a duplicate to be removed
                shift += 1
            else:
                # tracks 2 places behind k, and is adjusted for the shift
                i += 1

        # return the length of the new array
        return len(nums) - shift
