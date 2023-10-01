# Problem: https://leetcode.com/problems/distinct-subsequences/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        # set up base cases
        for i in range(len(s)+1):
            dp[(i, len(t))] = 1
        for j in range(len(t)):
            dp[(len(s), j)] = 0

        def solve(i, j):
            if (i, j) in dp:
                # cache hit
                return dp[(i, j)]

            if s[i] == t[j]:
                # try both consuming character, and not consuming to look for more options
                dp[(i, j)] = solve(i+1, j+1) + solve(i+1, j)
            else:
                # can't consume character
                dp[(i, j)] = solve(i+1, j)

            return dp[(i, j)]

        return solve(0, 0)
