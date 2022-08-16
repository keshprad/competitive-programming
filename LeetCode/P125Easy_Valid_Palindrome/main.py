# Problem: https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def isPalindrome2(self, s: str) -> bool:
        # convert to lowercase
        s = list(s.lower())
        # remove non-alphanumeric characters
        for i in range(len(s)):
            if not s[i].isalnum():
                s[i] = ''
        s = ''.join(s)

        # check palindrome
        return s == s[::-1]
