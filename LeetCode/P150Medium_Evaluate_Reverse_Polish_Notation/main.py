from typing import List
from collections import deque
# Problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/


class Solution:
    def add(self, a, b): return a + b

    def diff(self, a, b): return a - b

    def prod(self, a, b): return a * b

    def quotient(self, a, b): return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+': self.add, '-': self.diff,
                     '*': self.prod, '/': self.quotient}
        stack = deque()

        for token in tokens:
            if token in operators:
                b, a = stack.pop(), stack.pop()
                c = operators[token](a, b)
                stack.append(c)
            else:
                stack.append(int(token))
        return stack.pop()
