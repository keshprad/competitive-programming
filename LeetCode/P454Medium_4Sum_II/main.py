from typing import List
# Problem: https://leetcode.com/problems/4sum-ii/


class Solution:
    def fourSumCount(self,
                     nums1: List[int],
                     nums2: List[int],
                     nums3: List[int],
                     nums4: List[int],
                     target: int = 0) -> int:
        count = 0
        sum_counts = {}

        for a in nums1:
            for b in nums2:
                # Find all combos of a and b
                # Store the count of each 2sum in a dict
                sum_counts[a + b] = sum_counts.get(a + b, 0) + 1

        for c in nums3:
            for d in nums4:
                # target = a + b + c + d
                # Therefore a + b = target - c - d
                # If target - c - d exists, we add its count
                count += sum_counts.get(target - c - d, 0)

        return count
