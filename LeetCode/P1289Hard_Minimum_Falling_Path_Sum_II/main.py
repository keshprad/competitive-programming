import heapq
from typing import List
# Problem: https://leetcode.com/problems/minimum-falling-path-sum-ii/


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1, len(grid)):
            # Find the two smallest values of prev row
            sm = heapq.nsmallest(2, grid[i - 1])

            for j in range(len(grid[0])):
                # Add the smallest if it has a nonzero shift
                # Otherwise, add the 2nd smallest
                grid[i][j] += sm[0] if grid[i - 1][j] != sm[0] else sm[1]

        # Return the smallest val in the last row.
        return min(grid[-1])
