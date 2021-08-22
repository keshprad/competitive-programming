from typing import List
# Problem: https://leetcode.com/problems/add-to-array-form-of-integer/


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # Add k to the last element in num list
        num[-1] += k

        # Maintain a "carry" and move the 10s place until list is balanced
        carry = 0
        i = len(num) - 1
        while (num[i] >= 10 or carry) and i >= 0:
            carry, num[i] = divmod(num[i] + carry, 10)
            i -= 1

        # Handle any remaining value in carry
        carry_arr = []
        while carry:
            carry, remain = divmod(carry, 10)
            carry_arr.append(remain)

        # Reverse the carry array and prepend to num
        num = carry_arr[::-1] + num

        return num
