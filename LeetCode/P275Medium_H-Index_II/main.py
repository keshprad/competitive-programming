from typing import List
# Problem: https://leetcode.com/problems/h-index-ii/


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        r = len(citations) - 1
        n = len(citations)

        while l <= r:
            mid = (l + r) // 2
            h = n - mid

            if h > citations[mid]:
                l = mid + 1
            elif h < citations[mid]:
                r = mid - 1
            else:
                return citations[mid]
        return n - l
