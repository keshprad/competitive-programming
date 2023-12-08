# Problem: https://leetcode.com/problems/maximum-69-number/


class Solution:
    def maximum69Number(self, num: int) -> int:
        digit = -1
        i = 0
        temp = num
        while temp:
            if temp % 10 == 6:
                digit = i
            temp //= 10
            i += 1

        # no 6s in number
        if digit == -1:
            return num
        # found 6
        return num + 3*(10**digit)
