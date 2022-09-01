# Problem: https://leetcode.com/problems/valid-palindrome-ii/


class Solution:
    def validPalindrome2(self, s: str) -> bool:
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
                return isPalindrome(s[:l] + s[l+1:]) or isPalindrome(s[:r] + s[r+1:])

            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s: str, fail_expr=lambda l, r: False) -> bool:
            l, r = 0, len(s) - 1

            while l < r:
                if s[l] != s[r]:
                    return fail_expr(l, r)

                l += 1
                r -= 1
            return True

        return isPalindrome(s, lambda l, r: isPalindrome(s[:l] + s[l+1:]) or isPalindrome(s[:r] + s[r+1:]))
