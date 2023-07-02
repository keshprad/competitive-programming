from typing import List
# Problem: https://leetcode.com/problems/subsets-ii/description/


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()

        def dfs(i, subset):
            if i >= len(nums):
                return

            # include nums[i]
            res.append(subset+[nums[i]])
            dfs(i+1, res[-1])

            # don't include nums[i]
            # skip over all indices with this val
            num = nums[i]
            while 0 <= i < len(nums) and nums[i] == num:
                i += 1
            dfs(i, subset)

        dfs(0, [])
        return res
