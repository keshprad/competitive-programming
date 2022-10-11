from typing import List
# Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            B, A = A, B

        l = 0
        r = len(A) - 1
        while True:
            i = l + (r - l) // 2    # A
            j = half - i - 2        # B

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i+1] if i + 1 < len(A) else float('inf')

            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if j + 1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                # partition is valid
                if total % 2 == 1:
                    # odd
                    return min(Aright, Bright)
                else:
                    # even
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        if len(merged) == 0:
            return 0.0
        elif len(merged) % 2 == 0:
            return float(merged[len(merged) // 2] + merged[len(merged) // 2 - 1]) / 2
        else:
            return float(merged[len(merged) // 2])
