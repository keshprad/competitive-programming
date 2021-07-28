from typing import List
# Problem: https://leetcode.com/problems/n-queens/


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(solutions, queens, xy_diffs, xy_sums):
            row_idx = len(queens)

            if row_idx == n:
                solutions.append(queens)
                return
            
            for col_idx in range(n):
                # Check that col and diagonals not already used. 
                # Don't need to check row_idx as it'll only be seen once per queen added.
                if col_idx not in queens and row_idx - col_idx not in xy_diffs and row_idx + col_idx not in xy_sums:
                    # queens: Add new queen
                    # xy_diffs: Saving (x, y) diff. If the number appears again, it is a \ diagonal to (x, y)
                    # xy_sums: Saving (x, y) sum. If the number appears again, it is a / diagonal to (x, y)
                    DFS(solutions, queens + [col_idx], xy_diffs + [row_idx - col_idx], xy_sums + [row_idx + col_idx])
        
        solutions = []
        DFS(solutions, [], [], [])

        return [['.'*col + 'Q' + '.'*(n-col-1) for col in sol] for sol in solutions]
