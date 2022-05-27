from typing import List
# Problem: https://leetcode.com/problems/product-of-array-except-self/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """If it's confusing understanding this solution, look at 
        productExceptSelf2(), which breaks this solution down into steps.
        """
        output = []

        # prod of all nums before each index
        coeff = 1
        for num in nums:
            output.append(coeff)
            coeff *= num

        # go in reverse order, calculating prod of all nums after each index
        # mult prod before index by prod after index to get prod except self
        coeff = 1
        for i in range(-1, -len(nums)-1, -1):
            output[i] *= coeff
            coeff *= nums[i]

        return output

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        prod_before = []
        prod_after = []
        output = []

        # product of all nums before the each index
        coeff = 1
        for num in nums:
            prod_before.append(coeff)
            coeff *= num

        # product of all nums after each index
        coeff = 1
        for num in nums[::-1]:
            prod_after.append(coeff)
            coeff *= num
        # Reverse the list since going in reverse order
        prod_after = prod_after[::-1]

        # prod_before * prod_after = prod except self
        # do this for ever index
        for i in range(len(nums)):
            output.append(prod_before[i] * prod_after[i])

        return output
