# Problem: https://leetcode.com/problems/split-two-strings-to-make-palindrome/


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        # Find palidrome from prefix a and suffix b
        i, j = 0, len(b) - 1
        while i < j and a[i] == b[j]:
            i += 1
            j -= 1
        # Middle a and b
        mid1a, mid1b = a[i:j + 1], b[i:j + 1]

        # Find palidrome from prefix a and suffix b
        i, j = 0, len(a) - 1
        while i < j and b[i] == a[j]:
            i += 1
            j -= 1
        # Middle a and b
        mid2a, mid2b = a[i:j + 1], b[i:j + 1]

        # If any middle pieces are a palindrome, then palindrome formation is possible
        return any((mid == mid[::-1] for mid in (mid1a, mid1b, mid2a, mid2b)))
