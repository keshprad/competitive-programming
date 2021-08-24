# Problem: https://leetcode.com/problems/add-binary/


class Solution:
    # Iterative Solution
    def addBinary(self, a: str, b: str) -> str:
        bin_sum = ''
        a, b = map(list, (a, b))

        carry = 0
        while a or b:
            # Iterate through each index in reverse order
            num1 = int(a.pop()) if a else 0
            num2 = int(b.pop()) if b else 0

            # Calculate a carry and a val for the current index
            carry, val = divmod(num1 + num2 + carry, 2)
            bin_sum += str(val)

        # If a carry is leftover from the loop, add to bin_sum
        bin_sum += str(carry) if carry else ''

        # Reverse order since binary sum was calculated & stored in reverse order
        return bin_sum[::-1]
