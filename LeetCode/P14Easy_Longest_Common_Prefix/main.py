from typing import List
# Problem: https://leetcode.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""

        n = len(strs[0])
        for s in strs:
            n = min(len(s), n)

        i = 0
        while i < n:
            curr = strs[0][i]

            for s in strs:
                if s[i] != curr:
                    return strs[0][:i]
            i += 1
        return strs[0][:i] if i > 0 else ""
