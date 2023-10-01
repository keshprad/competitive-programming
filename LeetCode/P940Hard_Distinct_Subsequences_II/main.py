# Problem: https://leetcode.com/problems/distinct-subsequences-ii/

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        '''
        finding dp[i]:
        1. add char
            new combos = 2 * dp[i-1]

        2. consider new letter
            if s[i] is unseen, add 1 for the single character subseq

        3. remove duplicates
            dups = dp[j-1]
        - - a_j - a_i

        If we are adding a, the duplicates are all the combos from when the previous a was added.

        Therefore: dp[i] = 2 * dp[i-1] - dp[j-1]
        '''
        dp = {_: 0 for _ in range(len(s))}
        dp[-1] = 0

        # maintain dict of prev seen instances of each char
        prev = {}

        for i in range(0, len(s)):
            dp[i] = 2*dp[i-1]
            dp[i] += s[i] not in prev

            # index of previous instance of s[i]
            j = prev.get(s[i], 0)
            # remove duplicates
            dp[i] -= dp[j-1]

            # set prev for character i
            prev[s[i]] = i

        # return modulus
        return dp[len(s)-1] % (10**9+7)
