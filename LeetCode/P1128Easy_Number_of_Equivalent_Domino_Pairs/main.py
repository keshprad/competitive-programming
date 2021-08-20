from math import factorial
from typing import List
# Problem: https://leetcode.com/problems/number-of-equivalent-domino-pairs/


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = {}
        for a, b in dominoes:
            # If seen before, add 1 to its count
            if (a, b) in counts:
                counts[(a, b)] += 1
            # If rotated domino was seen before, add 1 to its count
            elif (b, a) in counts:
                counts[(b, a)] += 1
            # Create a new count if domino not seen before
            else:
                counts[(a, b)] = 1

        pairs = 0
        # Iterate through values and use num combinations formula to find number of pairs
        for i in counts.values():
            # Need 2 or more equivalent dominoes to form pairs
            if i >= 2:
                pairs += factorial(i) / (2 * factorial(i - 2))
        return int(pairs)


sol = Solution()
print(sol.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]))
print(sol.numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))
