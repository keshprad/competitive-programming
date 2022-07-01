from typing import List
# Problem: https://leetcode.com/problems/range-sum-query-2d-immutable/


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        # matrix of zeros with padding on top and left
        self.sums = [[0] * (len(matrix[0]) + 1)
                     for _ in range(len(matrix) + 1)]

        for r in range(1, len(matrix) + 1):
            for c in range(1, len(matrix[r-1]) + 1):
                self.sums[r][c] = self.sums[r-1][c] + self.sums[r][c -
                                                                   1] - self.sums[r-1][c-1] + matrix[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # adjust for padding
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        return self.sums[row2][col2] - self.sums[row2][col1 - 1] - self.sums[row1 - 1][col2] + self.sums[row1 - 1][col1 - 1]
