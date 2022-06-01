import numpy as np
from typing import List
# Problem: https://leetcode.com/problems/valid-sudoku/


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subs = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != '.':
                    s = 3 * (c // 3) + (r // 3)

                    if num in rows[r] or num in cols[c] or num in subs[s]:
                        return False
                    rows[r].add(num)
                    cols[c].add(num)
                    subs[s].add(num)
        return True
