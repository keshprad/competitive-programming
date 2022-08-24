from typing import List
from collections import deque
# Problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+': lambda a, b: a + b,
               '-': lambda a, b: a - b,
               '*': lambda a, b: a * b,
               '/': lambda a, b: int(a / b)}

        for token in tokens:
            if token in ops:
                b, a = stack.pop(), stack.pop()
                res = ops[token](a, b)
                stack.append(res)
            else:
                stack.append(int(token))

        return stack.pop()
