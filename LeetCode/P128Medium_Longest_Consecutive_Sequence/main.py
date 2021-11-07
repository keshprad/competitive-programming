from typing import List
# Problem: https://leetcode.com/problems/longest-consecutive-sequence/


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seq_len = 0

        for l in nums:
            # if l-1 is in nums, there is a longer seq
            # which we have already or will later see
            if l - 1 not in nums:
                r = l + 1
                while r in nums:
                    r += 1
                seq_len = max(seq_len, r - l)
        return seq_len
