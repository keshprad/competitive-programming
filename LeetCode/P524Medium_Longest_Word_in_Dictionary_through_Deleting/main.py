from typing import List
# Problem: https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary = sorted(dictionary, key=lambda w: (-len(w), w))

        for word in dictionary:
            i = 0
            # Let's go through every char in s
            for char in s:
                # if all chars in word are found, i will equal len(word)
                if char == word[i]:
                    i += 1
                # Word was found!
                if i == len(word):
                    return word
        return ''
