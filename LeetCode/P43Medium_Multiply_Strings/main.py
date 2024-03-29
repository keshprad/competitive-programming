# Problem: https://leetcode.com/problems/multiply-strings/


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Initialize to the max possible length for an NxM product
        # Will be the reversed product
        rev_prod = [0] * (len(num1) + len(num2))

        # res is generated in the opposite order
        for i, x in enumerate(num1[::-1]):
            for j, y in enumerate(num2[::-1]):
                # Uses ord because int is not allowed in the problem desc.
                # Adds product to the one's place for current index
                rev_prod[i + j] += (ord(x) - ord('0')) * (ord(y) - ord('0'))
                # Carry over the ten's place if applicable
                rev_prod[i + j + 1] += rev_prod[i + j] // 10
                # Use modulus 10 to find only the 1s place
                rev_prod[i + j] %= 10

        # Remove the zeros at end
        # These are the leading zeros in the final answer, since res is reveresed
        while len(rev_prod) > 1 and rev_prod[-1] == 0:
            rev_prod.pop()

        # Reverse the list, map ints to a string, and join list
        return ''.join(map(str, rev_prod[::-1]))
