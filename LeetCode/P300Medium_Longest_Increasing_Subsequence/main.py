from typing import List
from bisect import bisect_left
# Problem: https://leetcode.com/problems/longest-increasing-subsequence/


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # start array with first elem
        arr = [nums.pop(0)]

        for num in nums:
            if num > arr[-1]:
                # case 1: append elem to arr
                arr.append(num)
            else:
                # case 2: can't append elem to arr
                # instead, replace closest number greater
                arr[bisect_left(arr, num)] = num
        return len(arr)

    
    def lengthOfLIS2(self, nums: List[int]) -> int:
        dp = {}

        for i in range(len(nums)-1, -1, -1):
            dp[i] = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp.values())