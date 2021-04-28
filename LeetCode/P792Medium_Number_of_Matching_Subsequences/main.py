from typing import List
import collections
# Problem: https://leetcode.com/problems/number-of-matching-subsequences/


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = collections.defaultdict(list, {'-': map(iter, words)})
        for char in '-' + s:
            for word_iter in d.pop(char, ()):
                new_char = next(word_iter, None)
                d[new_char].append(word_iter)
        return len(d[None])
