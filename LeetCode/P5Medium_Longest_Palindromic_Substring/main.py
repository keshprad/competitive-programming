# Problem: https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # initial longest palindrome
        best = '' if not s else s[-1]
        # memo indicating whether substr spanning (i, j) is a palindrome
        # set all substrs of len 1 to palindromes
        dp = {(i, i): True for i in range(len(s))}

        for m in range(0, len(s)):
            # m is the middle of our palindrome

            l, r = m-1, m+1

            # if palindrome length not odd, our midpoint could be
            # an even amt of letters. Expand to include duplicates
            while l >= 0 and s[l] == s[m]:
                l -= 1
            while r < len(s) and s[r] == s[m]:
                r += 1
            dp[(l+1, r-1)] = True

            while l >= 0 and r < len(s):
                # expand outward (move l left and r right)
                dp[(l, r)] = dp[(l+1, r-1)] and s[l] == s[r]

                # no longer a palindrome
                if not dp[(l, r)]:
                    break

                l -= 1
                r += 1

            if len(best) < r - l - 1:
                best = s[l+1:r]

        return best
