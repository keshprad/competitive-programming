from typing import List
# Problem: https://leetcode.com/problems/game-of-life/


class Solution:
    # 0 -> 0: 0
    # 1 -> 1: 1
    # 1 -> 0: 2
    # 0 -> 1: 3
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return
        m, n = len(board), len(board[0])

        # changes cell states
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                count = self.live_neighbors(board, r, c)
                if board[r][c] == 1:
                    if count < 2 or count > 3:
                        board[r][c] = 2
                else:
                    if count == 3:
                        board[r][c] = 3

        # resets any temp values
        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1

    def live_neighbors(self, board: List[List[int]], r: int, c: int) -> int:
        m, n = len(board), len(board[0])
        live = 0
        for i in range(max(0, r-1), min(r+2, m)):
            for j in range(max(0, c-1), min(c+2, n)):
                if (i, j) != (r, c) and 1 <= board[i][j] <= 2:
                    live += 1
        return live
