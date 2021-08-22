from typing import List
# Problem: https://leetcode.com/problems/sort-colors/


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # zero and two are pointers to the index where 0s and 2s should be swapped.
        zero, two = 0, len(nums) - 1
        # pos is a pointer to the current index.
        pos = 0

        # Iterate through moving 0s to the left and 2s to the right.
        # This will leave the 1s in the center, and therefore sorts the array.
        while pos <= two:
            if nums[pos] == 0:
                # Swap current pos and zero pointer
                nums[pos], nums[zero] = nums[zero], nums[pos]
                # Move zero pointer forward one
                zero += 1
                # Keep pointer in place if the 0 is swapped into the current spot.
                pos -= nums[pos] != 0
            elif nums[pos] == 2:
                # Swap current pos and two pointer
                nums[pos], nums[two] = nums[two], nums[pos]
                # Move two pointer back one
                two -= 1
                # Move pointer back to keep inplace to check the swapped number
                pos -= 1
            pos += 1
