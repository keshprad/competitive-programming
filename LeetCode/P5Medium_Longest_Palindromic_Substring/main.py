# Problem: https://leetcode.com/problems/longest-palindromic-substring/solution/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal = ''

        for l in range(len(s)):
            for r in range(len(s), l, -1):
                # Check if the length is longer than the current palindrome
                # Check if it is a palindrome from index l to r
                if r - l > len(pal) and s[l:r] == s[l:r][::-1]:
                    pal = s[l:r]
                    break
        return pal
