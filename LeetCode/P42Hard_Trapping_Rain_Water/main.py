from typing import List
# Problem: https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        vol, l, r = 0, 0, len(height) - 1
        max_l, max_r = height[l], height[r]

        while l < r:
            max_l, max_r = max(max_l, height[l]), max(max_r, height[r])
            if max_l > max_r:
                vol += max_r - height[r]
                r -= 1
            else:
                vol += max_l - height[l]
                l += 1
        return vol
