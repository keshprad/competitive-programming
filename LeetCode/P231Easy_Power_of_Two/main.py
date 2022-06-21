# Problem: https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # n & (n-1) gets rid of the rightmost bit from a number
        # for powers of 2, n & (n-1) should be == 0
        # Special case for n <= 0 because of negative numbers.
        # However all powers of 2 are positive, so always false
        return not n & (n-1) if n > 0 else False
