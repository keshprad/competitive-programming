import string
# Problem: https://leetcode.com/problems/permutation-in-string/


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''O(n) time, O(26) space solution'''
        if len(s1) > len(s2):
            return False

        # find init counts of window
        s1_count = [0] * 26
        s2_count = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # find init matches of window
        matches = 0
        for i in range(26):
            matches += s1_count[i] == s2_count[i]

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            char = ord(s2[r]) - ord('a')
            s2_count[char] += 1
            if s1_count[char] == s2_count[char]:
                matches += 1
            elif s1_count[char] + 1 == s2_count[char]:
                matches -= 1

            char = ord(s2[l]) - ord('a')
            s2_count[char] -= 1
            if s1_count[char] == s2_count[char]:
                matches += 1
            elif s1_count[char] - 1 == s2_count[char]:
                matches -= 1
            l += 1
        return matches == 26

    def checkInclusion2(self, s1: str, s2: str) -> bool:
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
