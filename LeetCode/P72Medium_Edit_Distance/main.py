# Problem: https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        for i in range(len(word1) + 1):
            dp[(i, len(word2))] = len(word1) - i
        for j in range(len(word2) + 1):
            dp[(len(word1), j)] = len(word2) - j

        def minDist(i, j):
            # check cache
            if (i, j) in dp:
                return dp[(i, j)]

            if word1[i] == word2[j]:
                dp[(i, j)] = minDist(i+1, j+1)
            else:
                # remove letter, add letter, or replace character
                dp[(i, j)] = 1 + min(minDist(i+1, j),
                                     minDist(i, j+1), minDist(i+1, j+1))

            return dp[(i, j)]

        return minDist(0, 0)
