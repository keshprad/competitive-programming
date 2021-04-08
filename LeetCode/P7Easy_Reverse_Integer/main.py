# Problem: https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        isNeg = x < 0

        x = int(str(abs(x))[::-1])
        if isNeg:
            return self.overflow(-x)
        else:
            return self.overflow(x)

    def overflow(self, x):
        minx = -1 * (2 ** 31)
        maxx = (2 ** 31) - 1

        if x < minx or x > maxx:
            return 0
        else:
            return x
