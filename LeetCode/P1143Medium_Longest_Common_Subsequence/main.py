# Problem: https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}

        def lcs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) in dp:
                # cache hit
                return dp[(i, j)]

            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + lcs(i+1, j+1)
            else:
                dp[(i, j)] = max(lcs(i+1, j), lcs(i, j+1))

            return dp[(i, j)]

        return lcs(0, 0)
