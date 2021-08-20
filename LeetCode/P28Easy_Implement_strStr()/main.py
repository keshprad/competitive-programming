# Problem: https://leetcode.com/problems/implement-strstr/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Iterate through haystack with a window of len of needle
        for i in range(len(haystack) - len(needle) + 1):
            # If the current window is same as the haystack, return the index
            if haystack[i:i + len(needle)] == needle:
                return i
        # Needle not found
        return -1
