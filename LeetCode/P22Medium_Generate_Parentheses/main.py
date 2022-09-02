from typing import List
# Problem: https://leetcode.com/problems/generate-parentheses/


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(nopen, nclose):
            # valid if open == close == n
            if nopen == nclose == n:
                res.append("".join(stack))
                return

            # only add open parenthesis is open < n
            if nopen < n:
                stack.append("(")
                backtrack(nopen+1, nclose)
                stack.pop()

            # only add closing parenthesis if close < open
            if nclose < nopen:
                stack.append(")")
                backtrack(nopen, nclose+1)
                stack.pop()

        backtrack(0, 0)
        return res
