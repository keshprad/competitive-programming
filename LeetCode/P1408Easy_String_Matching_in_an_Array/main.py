from typing import List
# Problem: https://leetcode.com/problems/string-matching-in-an-array/


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()
        for i, sub in enumerate(words):
            for j, word in enumerate(words):
                if i != j and sub in word:
                    res.add(sub)
        return list(res)
