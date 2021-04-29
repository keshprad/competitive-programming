# Problem: https://leetcode.com/problems/search-a-2d-matrix/


from typing import List
import numpy as np
import bisect


class Solution:
    def searchMatrix_1(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False

        shape = len(matrix)*len(matrix[0])
        mat = np.reshape(matrix, newshape=shape)
        pos = bisect.bisect_left(mat, target)

        if pos == len(mat):
            # target larger than last element in mat
            return False
        return mat[pos] == target

    def searchMatrix_2(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0]:
            return False

        mat = np.array(matrix)
        row = bisect.bisect_right(mat[:, 0], target) - 1
        col = bisect.bisect_left(mat[row, :], target)

        if col == len(mat[row]):
            return False
        return mat[row, col] == target
