from typing import List
# Problem: https://leetcode.com/problems/palindrome-pairs/


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # Create a lookup dict to find index of any word
        lookup = {word: i for i, word in enumerate(words)}

        palindromes = []
        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                # Find prefix and suffix at every j index
                pref, suf = w[:j], w[j:]
                # If pref is a palindrome, and reverse of suf exists in lookup, we have a pair!
                # The pair is reverse suf + word
                if pref == pref[::-1] and suf[::-1] != w \
                    and suf[::-1] in lookup:
                    palindromes.append([lookup[suf[::-1]], i])

                # If suf is a palindrome, and reverse of pref exists in lookup, we have a pair
                # The pair is word + reverse pref
                if j != len(w) and suf == suf[::-1] and pref[::-1] in lookup:
                    palindromes.append([i, lookup[pref[::-1]]])
        return palindromes

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]
