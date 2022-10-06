# Problem: https://leetcode.com/problems/car-fleet/
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []

        for x, v in sorted(zip(position, speed), key=lambda x: x[0], reverse=True):
            time = (target - x)/v
            times.append(time)
            if len(times) >= 2 and times[-2] >= times[-1]:
                times.pop()
        return len(times)
