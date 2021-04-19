# Problem: https://leetcode.com/problems/remove-k-digits/


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for dig in num:
            while k and stack and stack[-1] > dig:
                stack.pop()
                k -= 1
            stack.append(dig)

        stack = stack[:-k] if k else stack
        stack = "".join(stack).lstrip('0')
        return stack if stack else '0'
