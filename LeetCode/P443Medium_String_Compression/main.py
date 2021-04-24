from typing import List
# Problem: https://leetcode.com/problems/string-compression/


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        l = r = 0
        while r < len(chars):
            while r < len(chars) and chars[l] == chars[r]:
                r += 1
            if r-l == 1:
                l = r
            else:
                chars[l+1:r] = str(r-l)
                l = r = l+2
