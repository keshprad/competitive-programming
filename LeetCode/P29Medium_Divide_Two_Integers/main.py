# Problem: https://leetcode.com/problems/divide-two-integers/


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Special case because of the way two's complement is repr.
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1

        # handle sign at end
        num, denom = abs(dividend), abs(divisor)
        res = 0

        # Iterate through all 2^31 to 2^0
        for i in range(32)[::-1]:
            # Check how much the numerator can be reduced and still be greater
            # than the denom
            if (num >> i) >= denom:
                # Essentially, num = denom * (1 << i) + rem
                # by subtracting denom << i, the next val of num is the
                # remainder.
                num -= denom << i
                # Update the quotient, adding the found multiple of denom that
                # can be subtracted from numerator
                res += 1 << i

        return res if (dividend > 0) == (divisor > 0) else -res


sol = Solution()
print(sol.divide(-2147483648, -2))
