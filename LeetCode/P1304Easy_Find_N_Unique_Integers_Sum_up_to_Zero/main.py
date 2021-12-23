from typing import List
# Problem: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/


class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []

        for i in range(n):
            # Every 2 elements have same magnitude opposite sign
            # This means ever 2 elements have a sum of zero
            if i % 2 == 0:
                res.append(i//2 + 1)
            else:
                res.append(-(i//2 + 1))

        # If an extra element at end, set to zero so sum is 0
        if n % 2 == 1:
            res[-1] = 0

        return res
