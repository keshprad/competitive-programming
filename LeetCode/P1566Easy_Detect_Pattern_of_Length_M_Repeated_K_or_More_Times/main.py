# Problem: https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/
from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        streak = 0
        for i in range(len(arr)-m):
            streak = streak + 1 if arr[i] == arr[i+m] else 0
            if streak == (k-1)*m:
                return True
        return False
