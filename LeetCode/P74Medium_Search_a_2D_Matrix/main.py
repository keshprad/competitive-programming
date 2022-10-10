# Problem: https://leetcode.com/problems/search-a-2d-matrix/


from typing import List
import numpy as np
import bisect


class Solution:
    def searchMatrix_1(self, matrix: List[List[int]], target: int) -> bool:
        flat = np.array(matrix).flatten()
        pos = bisect.bisect_left(flat, target)
        return False if pos == len(flat) or flat[pos] != target else True

    def searchMatrix_2(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0]:
            return False

        mat = np.array(matrix)
        row = bisect.bisect_right(mat[:, 0], target) - 1
        col = bisect.bisect_left(mat[row, :], target)

        if col == len(mat[row]):
            return False
        return mat[row, col] == target

    def searchMatrix_3(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(lst: List[int], target):
            l = 0
            r = len(lst) - 1

            while l < r:
                mid = l + (r - l) // 2

                if lst[mid] > target:
                    r = mid - 1
                elif lst[mid] < target:
                    l = mid + 1
                else:
                    return mid
            return l if lst[l] == target else None

        for row in matrix:
            if binary_search(row, target) is not None:
                return True
        return False
