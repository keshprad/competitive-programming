from typing import List
# Problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[l] <= nums[mid] <= nums[r]:
                # l is the minimum element
                return nums[l]
            elif nums[l] <= nums[mid] and nums[mid] >= nums[r]:
                l = mid + 1
            elif nums[l] >= nums[mid] and nums[mid] <= nums[r]:
                r = mid

        return nums[l]
