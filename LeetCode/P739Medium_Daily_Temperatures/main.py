from typing import List
# Problem: https://leetcode.com/problems/daily-temperatures/


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                low_i = stack.pop()
                res[low_i] = i - low_i
            stack.append(i)
        return res
