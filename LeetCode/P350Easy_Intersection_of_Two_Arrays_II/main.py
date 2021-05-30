from typing import List
# Problem: https://leetcode.com/problems/intersection-of-two-arrays-ii/


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i1 = i2 = 0
        res = []

        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] > nums2[i2]:
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                res.append(nums1[i1])
                i1 += 1
                i2 += 1
        return res
