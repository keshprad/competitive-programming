# Problem: https://leetcode.com/problems/decode-ways/


class Solution:
    def numDecodings(self, s: str) -> int:
        # Exit early if s is null or has len of 0
        if not s:
            return 0

        # Initialize dynamic programming array
        dp = [0] * len(s)
        dp[0] = int(s[0] != '0')

        for i in range(1, len(s)):
            # Either a 1 charater or 2 character string -> int is possible
            first, second = int(s[i]), int(s[i - 1:i + 1])
            # If 1 char between 1 & 9, take on all ways to decode from the previous spot
            if 1 <= first <= 9:
                dp[i] += dp[i - 1]
            # If 2 char between 10 & 26, take on all ways to decode from spot 2 indices behind
            if 10 <= second <= 26:
                dp[i] += dp[
                    i -
                    2] if i >= 2 else 1  # Prevent an index out of bounds exception

        return dp[-1]
