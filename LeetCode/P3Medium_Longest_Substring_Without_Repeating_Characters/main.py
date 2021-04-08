# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = ''
        max_len = 0

        for char in s:
            if char in used:
                max_len = max(max_len, len(used))
                used = used[used.index(char) + 1:]
            used += char
        return max(max_len, len(used))
