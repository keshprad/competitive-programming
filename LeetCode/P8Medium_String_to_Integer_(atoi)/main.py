# Problem: https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()
        start = -1

        for s in range(len(str)):
            if str[s].isdigit():
                start = s
                break

        if start > 0 and (str[0] == "+" or str[0] == "-"):
            hasSign = 1
        else:
            hasSign = 0

        if start != hasSign:
            return 0

        end = len(str)
        for e in range(hasSign, len(str)):
            if not str[e].isdigit():
                end = e
                break

        if start == 1:
            return self.overflow(int(str[start - 1:end]))
        return self.overflow(int(str[start:end]))

    def overflow(self, x):
        minx = -1 * (2 ** 31)
        maxx = (2 ** 31) - 1

        if x < minx:
            return minx
        elif x > maxx:
            return maxx
        else:
            return x
