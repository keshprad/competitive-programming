from typing import List
# Problem: https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for i in range(len(nums)):
            item = nums[i]

            if target - item not in diff:
                diff[item] = i
            else:
                return [diff[target - item], i]
