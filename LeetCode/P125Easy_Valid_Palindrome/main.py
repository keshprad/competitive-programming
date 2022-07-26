# Problem: https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert to lowercase
        s = list(s.lower())
        # remove non-alphanumeric characters
        for i in range(len(s)):
            if not s[i].isalnum():
                s[i] = ''
        s = ''.join(s)

        # check palindrome
        return s == s[::-1]
