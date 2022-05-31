# Problem: https://leetcode.com/problems/reverse-bits/


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        if n:
            for i in range(32):
                res <<= 1
                res += n & 1
                n >>= 1
        return res
