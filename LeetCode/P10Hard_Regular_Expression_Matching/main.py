# Problem: https://leetcode.com/problems/regular-expression-matching/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # (i, j) -> bool indicating whether we can match rest of pattern
        dp = {}

        def match(i, j):
            # perform bounds checks
            # match to pattern (or wildcard)
            return 0 <= i < len(s) and 0 <= j < len(p) and \
                (s[i] == p[j] or p[j] == '.')

        def dfs(i, j):
            '''
            i = pointer in string s
            j = pointer in pattern p
            '''
            if i >= len(s) and j >= len(p):
                return True
            # don't need to check for either i or j out of bounds. This will
            # be caught in match and appropriately recurse is the pattern has a
            # following '?*' pattern
            if (i, j) in dp:
                return dp[(i, j)]

            if j+1 < len(p) and p[j+1] == '*':
                print()
                # three cases:
                # 1. consume char if equal, and move to next pattern
                # 2. consume char if equal, and repeat pattern
                # 3. don't consume char and move to next pattern
                # case 1 and 2 can be combined as shown below
                dp[(i, j)] = (match(i, j) and
                              (dfs(i+1, j+2) or dfs(i+1, j))) or \
                    dfs(i, j+2)
            else:
                # match char or '.' and recurse after consuming
                dp[(i, j)] = match(i, j) and dfs(i+1, j+1)
            return dp[(i, j)]

        return dfs(0, 0)
