# Problem: https://leetcode.com/problems/clumsy-factorial/
# Explanation: https://leetcode.com/problems/clumsy-factorial/discuss/252279/You-never-think-of-this-amazing-O(1)-solution

class Solution:
    def clumsy(self, n: int) -> int:
        # Cases where n < 5
        if n <= 2:
            return n
        if 3 <= n <= 4:
            return n + 3

        # Cases where n >= 5
        if n % 4 == 0:
            return n + 1
        if n % 4 <= 2:
            return n + 2
        if n % 4 == 3:
            return n - 1
