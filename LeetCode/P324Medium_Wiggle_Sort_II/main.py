from typing import List
# Problem: https://leetcode.com/problems/wiggle-sort-ii/


class Solution:
    # Solution with O(nlogn) time complexity and
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Sort the list
        nums.sort()
        mid = len(nums[::2])
        # Move the larger half of the array to be alternating with smaller half of array
        # Reverse the halves, which solves duplicate middle elements. eg: [1, 2, 2, 3] -> [2, 3, 2, 1]
        nums[1::2], nums[::2] = nums[mid:][::-1], nums[:mid][::-1]
