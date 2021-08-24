from typing import List
# Problem: https://leetcode.com/problems/plus-one/


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while carry and i >= 0:
            carry, digits[i] = divmod(digits[i] + carry, 10)
            i -= 1

        return [carry, *digits] if carry else digits
