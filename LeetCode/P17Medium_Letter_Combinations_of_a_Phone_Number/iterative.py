from collections import deque
from typing import List
# Problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class IterativeSolution:
    def __init__(self):
        self.mappings = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        combos = deque()
        for letter in self.mappings[digits[0]]:
            combos.append(letter)

        for i in range(1, len(digits)):
            for c in range(len(combos)):
                combo = combos.popleft()
                for letter in self.mappings[digits[i]]:
                    combos.append(combo+letter)
        return combos
