# Problem: https://leetcode.com/problems/hamming-distance/


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        while x or y:
            dist += (x & 1) != (y & 1)
            x >>= 1
            y >>= 1
        return dist
