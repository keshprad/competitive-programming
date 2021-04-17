from collections import deque


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length, stack = 0, deque([-1])
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif stack:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        return max_length
