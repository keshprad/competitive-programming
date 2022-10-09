# Problem: https://leetcode.com/problems/largest-rectangle-in-histogram/
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for r, hr in enumerate(heights):
            start = r
            while stack and stack[-1][1] > hr:
                l, hl = stack.pop()
                max_area = max(max_area, hl * (r - l))
                start = l
            stack.append((start, hr))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area
