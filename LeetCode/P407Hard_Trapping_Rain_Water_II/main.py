from typing import List
import heapq
# Problem: https://leetcode.com/problems/trapping-rain-water-ii/


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or len(heightMap) < 3:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        heap, volume = [], 0

        for row in range(m):
            for col in range(n):
                if row in {0, m-1} or col in {0, n-1}:
                    heapq.heappush(heap, (heightMap[row][col], row, col))
                    heightMap[row][col] = -1

        while heap:
            height, row, col = heapq.heappop(heap)
            for r, c in ((row, col-1), (row, col+1), (row-1, col), (row+1, col)):
                if 0 < r < m-1 and 0 < c < n-1 and heightMap[r][c] != -1:
                    volume += max(height - heightMap[r][c], 0)
                    heapq.heappush(heap, (max(heightMap[r][c], height), r, c))
                    heightMap[r][c] = -1
        return volume
