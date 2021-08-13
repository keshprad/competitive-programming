from typing import List
# Problem: https://leetcode.com/problems/check-if-it-is-a-straight-line/


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[:2]
        for x, y in coordinates:
            if (y - y0) * (x1 - x0) != (y1 - y0) * (x - x0):
                return False
        return True
