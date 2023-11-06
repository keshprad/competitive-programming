from typing import List
# Problem: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        m, n = len(matrix), len(matrix[0])

        def dfs(i, j, prev):
            if (not 0 <= i < m) or (not 0 <= j < n) or matrix[i][j] <= prev:
                # fell out of grid or path is not increasing
                return 0
            if (i, j) in dp:
                # return cache
                return dp[(i, j)]

            res = 1
            for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                # attempt moving every direction
                res = max(res, 1+dfs(i+dx, j+dy, matrix[i][j]))
            dp[(i, j)] = res
            return res

        # run dfs at each position.
        # Due to caching, each position (i, j) will only be calculated once
        # Therefore, O(m x n) time and space complexity
        for i in range(m):
            for j in range(n):
                dfs(i, j, -1)
        return max(dp.values())
