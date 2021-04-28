from typing import List
# Problem: https://leetcode.com/problems/minimum-area-rectangle/


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        graph = set(map(tuple, points))
        area = float('inf')

        for i, (x1, y1) in enumerate(points):
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in graph and (x2, y1) in graph:
                        curr_area = abs(x1 - x2) * abs(y1 - y2)
                        area = min(curr_area, area)
        return area if area < float('inf') else 0
