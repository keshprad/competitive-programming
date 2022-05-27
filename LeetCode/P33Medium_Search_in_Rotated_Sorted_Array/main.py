from typing import List
# Problem: https://leetcode.com/problems/search-in-rotated-sorted-array/


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] <= nums[r]:
                # nums is increasing from mid to r.
                # the partition is somewhere between l and mid

                if nums[mid] < target <= nums[r]:
                    # if target in nums, it's in right half
                    l = mid + 1
                else:
                    # if target in nums, it's in left half
                    r = mid - 1
            else:
                # nums is increasing from l to mid
                # the partition is somewhere between mid and r

                if nums[l] <= target < nums[mid]:
                    # if target in nums, its in left half
                    r = mid - 1
                else:
                    # if target in nums, it's in right half
                    l = mid + 1

        # target not found
        return -1
