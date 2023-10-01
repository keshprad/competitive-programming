# Problem: https://leetcode.com/problems/longest-palindromic-subsequence/


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        dp = {}
        for i in range(len(s)+1):
            dp[(i, len(t))] = 0
        for j in range(len(t)+1):
            dp[(len(s), j)] = 0

        def lcs(i, j):
            if (i, j) in dp:
                # cache hit
                return dp[(i, j)]

            if s[i] == t[j]:
                dp[(i, j)] = 1 + lcs(i+1, j+1)
            else:
                dp[(i, j)] = max(lcs(i+1, j), lcs(i, j+1))
            return dp[(i, j)]

        # problem reduces to LCS with the reversed of s
        return lcs(0, 0)
