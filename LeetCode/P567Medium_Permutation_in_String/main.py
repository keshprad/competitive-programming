import string
# Problem: https://leetcode.com/problems/permutation-in-string/


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''O(26n) time, O(26) space solution'''
        def get_counts(s: str) -> dict:
            d = {c: 0 for c in string.ascii_lowercase}
            for c in s:
                d[c] += 1
            return d

        if len(s1) > len(s2):
            return False

        l = 0
        r = len(s1) - 1
        # check init window
        d1 = get_counts(s1)
        d2 = get_counts(s2[l:r+1])
        if d1 == d2:
            return True

        # slide window and check
        while r < len(s2) - 1:
            d2[s2[l]] -= 1
            l += 1
            r += 1
            d2[s2[r]] += 1

            if d1 == d2:
                return True

        return False
