# Problem: https://leetcode.com/problems/sum-of-two-integers/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bit integer max
        MAX = 0x7FFFFFFF
        # 32 bit integer min
        MIN = 0x80000000

        # mask of all 1s for a 32 bit int
        mask = 0xffffffff
        while b:
            # ^ gets sum and & gets carry (which needs to be shifted by 1)
            # mask it to a 32 bit int
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # if the number is negative, we mask it to only include the first 32 bits
        return a if a <= MAX else a ^ ~mask
