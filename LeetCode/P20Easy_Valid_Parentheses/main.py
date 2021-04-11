from collections import deque
# Problem: https://leetcode.com/problems/valid-parentheses/


class Solution:
    def __init__(self):
        self.par_stack = deque()
        self.pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

    def isValid(self, s: str) -> bool:
        for par in s:
            if par in self.pairs:
                # if stack is empty
                if not self.par_stack:
                    return False
                # if popped isn't opening for par
                elif self.par_stack.pop() != self.pairs[par]:
                    return False
            else:
                self.par_stack.append(par)
        # returns false if stack still has parenthesis that were never closed
        return not self.par_stack
