from typing import List
# Problem: https://leetcode.com/problems/next-permutation/


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Start from end of permutation
        # Find the first number than the one just after it.
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1

        # If entire list is decreasing (i = 0), no possible next permutation
        # Using i <= 0 so to include cases for len(nums) == 1 or 0
        if i <= 0:
            # Reverse to get lowest possible permutation.
            nums.reverse()
        elif i == len(nums) - 1:
            # If list is increasing, just swap last 2 elements
            nums[-1], nums[-2] = nums[-2], nums[-1]
        else:
            swap = i
            i -= 1

            # Find the lowest element to the right of i that is greater than element at i
            for j in range(i+1, len(nums)):
                swap = j if nums[swap] > nums[j] > nums[i] else swap

            # Reorder list according to the swap
            nums[i:] = [nums[swap]] + \
                sorted(nums[i:swap] + nums[swap+1:])
