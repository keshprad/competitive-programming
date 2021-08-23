# Problem: https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bin_sum = ''
        a, b = map(list, (a, b))

        carry = 0
        while a or b:
            num1 = int(a.pop()) if a else 0
            num2 = int(b.pop()) if b else 0

            carry, rem = divmod(num1 + num2 + carry, 2)
            bin_sum += str(rem)

        bin_sum += str(carry) if carry else ''

        return bin_sum[::-1]
