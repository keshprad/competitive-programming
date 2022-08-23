from typing import List
from collections import deque
# Problem: https://leetcode.com/problems/sliding-window-maximum/


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        indQ = deque()
        valQ = deque()

        for i, num in enumerate(nums):
            while valQ and num > valQ[-1]:
                valQ.pop()
                indQ.pop()

            valQ.append(num)
            indQ.append(i)

            while i - indQ[0] + 1 > k:
                indQ.popleft()
                valQ.popleft()
            if i + 1 >= k:
                res.append(valQ[0])

        return res
