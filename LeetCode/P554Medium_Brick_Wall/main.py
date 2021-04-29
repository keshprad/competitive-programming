# Problem: https://leetcode.com/problems/brick-wall/


from typing import List
from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = defaultdict(int)
        max_edges = 0

        for layer in wall:
            vert_line = 0
            for brick in layer[:-1]:
                vert_line += brick
                edges[vert_line] += 1
                max_edges = max(max_edges, edges[vert_line])
        return len(wall) - max_edges
