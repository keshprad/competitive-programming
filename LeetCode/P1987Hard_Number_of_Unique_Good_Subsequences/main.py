class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        dp = {i: 0 for i in range(len(binary))}
        dp[-1] = 0

        for i in range(len(binary)):
            if binary[i] == '1':
                dp[i] = 1
                break

        prev0 = 0
        prev1 = i
        for i in range(i+1, len(binary)):
            # add new combinations
            dp[i] = 2*dp[i-1]

            # subtract duplicates
            if binary[i] == '0':
                dp[i] -= dp[prev0 - 1]
                prev0 = i
            else:
                dp[i] -= dp[prev1 - 1]
                prev1 = i

        has0 = '0' in binary
        mod = 10**9 + 7
        return (dp[len(binary)-1] + has0) % mod
