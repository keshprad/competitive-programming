from typing import List
# Problem: https://leetcode.com/problems/fruit-into-baskets/


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        baskets, l = {}, 0

        for fruit in tree:
            baskets[fruit] = baskets.get(fruit, 0) + 1
            if len(baskets) > 2:
                baskets[tree[l]] -= 1
                if baskets[tree[l]] == 0:
                    del baskets[tree[l]]
                l += 1
        return len(tree) - l
