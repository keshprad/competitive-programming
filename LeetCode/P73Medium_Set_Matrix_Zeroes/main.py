from typing import List
# Problem: https://leetcode.com/problems/set-matrix-zeroes


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        # Remember whether 1st col and 1st row should be all zeros
        col1 = any(matrix[i][0] == 0 for i in range(m))
        row1 = any(matrix[0][j] == 0 for j in range(n))

        # If a point (i, j) is 0, set respective col1 and row1 to 0
        # We remember whether to set col1 and row1 to all 0s, so overwriting is fine
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # If the edge is a zero, the cell must also be set to zero
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # If original matrix had 0s in col1, set entire col to zeros
        if col1:
            for i in range(m):
                matrix[i][0] = 0

        # If original matrix had 0s in row1, set entire row to zeros
        if row1:
            for j in range(n):
                matrix[0][j] = 0
