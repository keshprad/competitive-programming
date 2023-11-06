# Problem: https://leetcode.com/problems/interleaving-string/


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}

        def isInterleave(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i >= len(s1):
                return s2[j:] == s3[i+j:]
            if j >= len(s2):
                return s1[i:] == s3[i+j:]

            dp[(i, j)] = (s1[i] == s3[i+j] and isInterleave(i+1, j)) \
                or (s2[j] == s3[i+j] and isInterleave(i, j+1))
            return dp[(i, j)]
        return (len(s3) == len(s1) + len(s2)) and isInterleave(0, 0)
