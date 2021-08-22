from typing import Tuple
# Problem: https://leetcode.com/problems/add-strings/


class Solution:
    # Solution using prepended zeros
    # O(n) space and time complexity
    def addStrings(self, num1: str, num2: str) -> str:
        # Prepend 0s to make num1 and num2 the same length
        num1, num2 = self.prependZeros(num1, num2)
        n = len(num1)

        # Initialize to the max possible length of the answer
        sum_arr = [0] * (n + 1)

        for i in range(-1, -len(sum_arr), -1):
            # Add the sum if index i at num1 and num2
            # Use ord since converting str to int directly is not allowed in problem desc.
            sum_arr[i] += self.get_int(num1[i]) + self.get_int(num2[i])
            # Carry over the tens place
            sum_arr[i - 1] += sum_arr[i] // 10
            # Use mod 10 on index i to leave only the one's place
            sum_arr[i] %= 10

        # Remove any leading 0s
        while len(sum_arr) > 1 and sum_arr[0] == 0:
            sum_arr.pop(0)

        return ''.join(map(str, sum_arr))

    # Function to prepend zeros to the shorter number
    def prependZeros(self, num1: str, num2: str) -> Tuple[str, str]:
        while len(num1) > len(num2):
            num2 = '0' + num2
        while len(num2) > len(num1):
            num1 = '0' + num1
        return num1, num2

    # Helper function to convert a string number to an int using ord()
    def get_int(self, num: str) -> int:
        return ord(num) - ord('0')

    # 2nd, more concise, solution
    # Has the same O(n) space and time complexity
    def addStrings2(self, num1: str, num2: str) -> str:
        nums1, nums2 = list(num1), list(num2)
        sum_arr = []
        carry = 0

        while nums1 or nums2:
            # If possible, pop last number. Otherwise, use zero to avoid None errors.
            n1 = self.get_int(nums1.pop()) if nums1 else 0
            n2 = self.get_int(nums2.pop()) if nums2 else 0

            carry, remainder = divmod(n1 + n2 + carry, 10)
            sum_arr.append(remainder)

        # If a carry exists, we need to append it
        if carry: sum_arr.append(carry)

        return ''.join(map(str, sum_arr))[::-1]


sol = Solution()
print(sol.addStrings(num1="11", num2="123"))  # Expected: '134'
print(sol.addStrings(num1="456", num2="77"))  # Expected: '533'
print(sol.addStrings(num1="0", num2="0"))  # Expected: '0'