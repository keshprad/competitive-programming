# Problem: https://leetcode.com/problems/different-ways-to-add-parentheses/
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        dp = {}
        ops = {
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '*': lambda a, b: a*b
        }

        def compute_list(op, lst1, lst2):
            res = []
            for i in lst1:
                for j in lst2:
                    res.append(op(i, j))
            return res

        def compute(i, j):
            res = []
            if (i, j) in dp:
                return dp[(i, j)]

            if expression[i:j+1].isnumeric():
                res.append(int(expression[i:j+1]))
            else:
                # expr has operations
                for k in range(i, j+1):
                    if expression[k] in ops:
                        res.extend(compute_list(
                            ops[expression[k]], compute(i, k-1), compute(k+1, j)))
            dp[(i, j)] = res
            return dp[(i, j)]
        return compute(0, len(expression)-1)
