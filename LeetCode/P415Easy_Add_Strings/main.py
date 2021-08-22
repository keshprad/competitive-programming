from typing import Tuple
# Problem: https://leetcode.com/problems/add-strings/


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Prepend 0s to make num1 and num2 the same length
        num1, num2 = self.prependZeros(num1, num2)
        n = len(num1)

        # Initialize to the max possible length of the answer
        sum_arr = [0] * (n + 1)

        for i in range(-1, -len(sum_arr), -1):
            # Add the sum if index i at num1 and num2
            # Use ord since converting str to int directly is not allowed in problem desc.
            sum_arr[i] += (ord(num1[i]) - ord('0')) + (ord(num2[i]) - ord('0'))
            # Carry over the tens place
            sum_arr[i - 1] += sum_arr[i] // 10
            # Use mod 10 on index i to leave only the one's place
            sum_arr[i] %= 10

        # Remove any leading 0s
        while len(sum_arr) > 1 and sum_arr[0] == 0:
            sum_arr.pop(0)

        return ''.join(map(str, sum_arr))

    def prependZeros(self, num1: str, num2: str) -> Tuple[str, str]:
        while len(num1) > len(num2):
            num2 = '0' + num2
        while len(num2) > len(num1):
            num1 = '0' + num1
        return num1, num2
