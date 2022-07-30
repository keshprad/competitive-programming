from typing import List
# Problem: https://leetcode.com/problems/word-search/


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i: int, j: int, board: List[List[str]], word: str) -> bool:
            if len(word) == 0:
                return True

            res = False
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[0]:
                temp = board[i][j]
                # prevent repetition of i, j position
                board[i][j] = '#'
                res = dfs(i-1, j, board, word[1:]) or dfs(i+1, j, board, word[1:]) \
                    or dfs(i, j-1, board, word[1:]) or dfs(i, j+1, board, word[1:])
                # reset position to original value
                board[i][j] = temp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, board, word):
                    return True
        return False
