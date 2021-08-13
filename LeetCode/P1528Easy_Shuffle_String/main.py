from typing import List
# Problem https://leetcode.com/problems/shuffle-string/


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for char, ind in zip(s, indices):
            res[ind] = char
        return ''.join(res)