from typing import List
# Problem: https://leetcode.com/problems/contains-duplicate/


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
