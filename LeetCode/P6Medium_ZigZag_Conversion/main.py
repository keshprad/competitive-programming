# Problem: https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Quick exit case
        if numRows == 1:
            return s

        res, i = "", 0
        max_space = 2 * numRows - 2

        # Compute spacing
        spacing = []
        for i in range(numRows):
            if max_space == 2 * i or 2 * i == 0:
                spacing.append([max(2 * i, max_space)])
            else:
                spacing.append([max_space - 2 * i, 2 * i])

        # Using spacing to find ZigZag pattern
        for i in range(numRows):
            k = i
            while k < len(s):
                res += s[k]
                k += spacing[i][0]
                if k < len(s) and len(spacing[i]) == 2:
                    res += s[k]
                    k += spacing[i][1]
        return res
