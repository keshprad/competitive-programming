from typing import List
# Problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class RecursiveSolution:
    def __init__(self):
        self.combos = []
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
        if len(digits) == 0:
            return []
        self.findCombos(digits)
        return self.combos

    def findCombos(self, digits: str, current: str = "", i: int = 0):
        if i == len(digits):
            self.combos.append(current)
        else:
            for mapping in self.mappings[digits[i]]:
                self.findCombos(digits, current=current+mapping, i=i+1)
