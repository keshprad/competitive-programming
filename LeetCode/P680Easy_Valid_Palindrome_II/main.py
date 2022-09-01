# Problem: https://leetcode.com/problems/valid-palindrome-ii/


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s: str) -> bool:
            l, r = 0, len(s) - 1

            while l < r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return isPalindrome(s[l:r]) or isPalindrome(s[l+1:r+1])

            l += 1
            r -= 1
        return True
