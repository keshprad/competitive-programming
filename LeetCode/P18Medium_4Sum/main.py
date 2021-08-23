from typing import List
# Problem: https://leetcode.com/problems/4sum/


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort nums and run k_sum with k = 4
        nums.sort()
        return self.k_sum(4, nums, target)

    def k_sum(self, k: int, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # Early exit cases where a ksum is not possible
        if not nums or sum(nums[:k]) > target or sum(nums[-k:]) < target:
            return res
        # For k = 2, we use the two sum method
        elif k == 2:
            return self.two_sum(nums, target)

        # Iterate through all possible values for one number in the k_sum
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                # Skip the number if it is already seen in a previous k_sum
                continue
            else:
                # Recursively call for k-1 sum.
                # Add the current value (nums[i]) to each solution and append them to results list
                for subset in self.k_sum(k - 1, nums[i + 1:],
                                         target - nums[i]):
                    res.append([nums[i], *subset])
        return res

    def two_sum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # Maintain a left and right pointer
        l, r = 0, len(nums) - 1

        while l < r:
            # nums is sorted. decreasing r decreases the sum. increasing l increases the sum
            curr_sum = nums[l] + nums[r]
            # when curr_sum > target, we can decrease index r
            if curr_sum < target:
                l += 1
            # when curr_sum < target, we can increase index l
            elif curr_sum > target:
                r -= 1
            else:
                # two_sum solution found.
                res.append([nums[l], nums[r]])
                # Iterate if duplicate l elements exist
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                # Iterate if duplicate r elements exist
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
        return res
