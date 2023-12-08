# Problem: https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/
from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        # ensure nums1 has larger sum
        tot1, tot2 = sum(nums1), sum(nums2)
        if tot1 < tot2:
            tot1, tot2 = tot2, tot1
            nums1, nums2 = nums2, nums1
        diff = tot1-tot2

        l = 0               # ptr in nums2
        r = len(nums1)-1    # ptr in nums1
        ops = 0
        while diff > 0 and ((0 <= l < len(nums2) and nums2[l] < 6) or
                            (0 <= r < len(nums1) and nums1[r] > 1)):
            cand1 = nums1[r] if 0 <= r < len(nums1) else 1
            cand2 = nums2[l] if 0 <= l < len(nums2) else 6
            if cand1-1 > 6-cand2:
                # changing nums1 brings sums closer
                nums1[r] = 1
                diff -= cand1-1
                r -= 1
            else:
                # changing nums2 brings sums closer
                nums2[l] = 6
                diff -= 6-cand2
                l += 1
            ops += 1

        return ops if diff <= 0 else -1
