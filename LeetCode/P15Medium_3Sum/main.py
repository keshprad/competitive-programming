from typing import List
# Problem: https://leetcode.com/problems/3sum/


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            # skip dup nums[i] vals
            if i == 0 or nums[i - 1] != nums[i]:
                l, r = i + 1, len(nums) - 1

                while l < r:
                    total = num + nums[l] + nums[r]
                    if total < 0:
                        l += 1
                    elif total > 0:
                        r -= 1
                    else:
                        # Found one solution.
                        # this nums[i] value can still have more solutions
                        res.append([nums[i], nums[l], nums[r]])

                        # skip dup nums[l] vals
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        # inc 1 more after to get the new val
                        l += 1

                        # skip dup nums[r] vals
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        # dec 1 more after to get the new val
                        r -= 1

        return res
