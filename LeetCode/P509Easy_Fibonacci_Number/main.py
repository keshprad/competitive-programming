# Problem: https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        n1 = n2 = 1

        for i in range(3, n+1):
            n1, n2 = n2, n1+n2
        return n2
