from collections import deque
# Problem: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/


class Solution(object):
    def removeDuplicates(self, s, k):
        stack = []
        for char in s:
            if len(stack) == 0 or stack[-1][0] != char:
                stack.append([char, 1])
            else:
                stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()

        res = ""
        for char, freq in stack:
            res += char*freq
        return res
