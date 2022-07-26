from typing import List
# Problem: https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # keep track of leftmost zero
        l_zero = 0
        for r in range(len(nums)):
            # similar to quicksort, swap non-zeros with partition(leftmost zero) left
            # this will move non-zeros to the left and guarantees next element after a swap is a zero.
            if nums[r] != 0:
                nums[r], nums[l_zero] = nums[l_zero], nums[r]
                l_zero += 1
