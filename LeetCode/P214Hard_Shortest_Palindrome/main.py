# Problem: https://leetcode.com/problems/shortest-palindrome/


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Find the longest palindrome that starts at the 0th index
        i = 0
        for j in range(len(s) - 1, -1, -1):
            i += s[i] == s[j]

        # Entire s is a palindrome
        if i == len(s):
            return s

        # At this point, i points to an index which doesn't conform to the palindrome.
        #
        # Since we can only add letters to the front of the string,
        # we can reverse the last portion of s and prepend it.
        #
        # The middle portion from 0:i may or may not be a palindrome,
        # so we recursively find the shortestPalindrome of this section.
        return s[i:][::-1] + self.shortestPalindrome(s[0:i]) + s[i:]

    def is_palindrome(self, s):
        return s == s[::-1]
