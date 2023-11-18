# Problem: https://leetcode.com/problems/maximal-square/
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        max_len = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                # use i-1, j-1 to index matrix bc dp array is padded
                if matrix[i-1][j-1] == '1':
                    # can make a len 1 square by itself
                    # or combining with the 3 around, it can make a bigger square
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                max_len = max(max_len, dp[i][j])

        # calc and return area from side length
        return max_len**2
