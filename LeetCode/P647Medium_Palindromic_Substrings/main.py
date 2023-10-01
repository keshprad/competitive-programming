# Problem: https://leetcode.com/problems/palindromic-substrings/


class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = {(i, i): True for i in range(len(s))}

        for m in range(len(s)):
            l, r = m-1, m+1

            while l >= 0 and s[l] == s[m]:
                dp[(l, m)] = True
                l -= 1
            while r < len(s) and s[r] == s[m]:
                dp[(m, r)] = True
                r += 1

            while l >= 0 and r < len(s):
                dp[(l, r)] = dp[(l+1, r-1)] and s[l] == s[r]

                if not dp[(l, r)]:
                    break

                l -= 1
                r += 1

        return sum(dp.values())
