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
            # Either a 1 digit or 2 digit string -> int is possible
            one_digit, two_digit = int(s[i]), int(s[i - 1:i + 1])
            # If 1 digit between 1 & 9, take on all ways to decode from 1 index behind
            if 1 <= one_digit <= 9:
                # Extends from 1 indices behind
                dp[i] += dp[i - 1]
            # If 2 digits between 10 & 26, take on all ways to decode from spot 2 indices behind
            if 10 <= two_digit <= 26:
                # Prevent an index out of bounds exception
                # Extends from 2 indices behind
                dp[i] += dp[i - 2] if i >= 2 else 1

        return dp[-1]
