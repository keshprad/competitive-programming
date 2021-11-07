from typing import List
# Problem: https://leetcode.com/problems/minimum-falling-path-sum/


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # DP approach where we alter the matrix to include the min falling path at each level
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                i_pos = max(i-1, 0)
                j_left = max(j-1, 0)
                j_right = min(j+1, len(matrix[0]) - 1)

                # The value is now (i,j) + the minimum of the (i-1,j-1), (i-1,j), (i-1, j+1)
                # Use bounded indices calculated above to prevent index out of bounds
                matrix[i][j] += min(matrix[i_pos][j_left],
                                    matrix[i_pos][j], matrix[i_pos][j_right])

        # The min of the last row
        return min(matrix[-1])
