from typing import List
# Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        if len(merged) == 0:
            return 0.0
        elif len(merged) % 2 == 0:
            return float(merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2
        else:
            return float(merged[len(merged) // 2])
