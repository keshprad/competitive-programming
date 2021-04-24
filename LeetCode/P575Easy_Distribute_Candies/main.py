from typing import List
# Problem: https://leetcode.com/problems/distribute-candies/


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType)//2)
