from collections import deque
from typing import List
# Problem: https://leetcode.com/problems/permutations-ii/


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = deque([[]])

        # Try to insert each num into our current perms
        for num in nums:
            for _ in range(len(perms)):
                # overwrite the list as we popleft the current n elements and add new permutations.
                perm = perms.popleft()

                for i in range(len(perm) + 1):
                    # Shift num into each position in this permutation.
                    perms.append(perm[:i] + [num] + perm[i:])
                    # If the prev element is the same as current, break early.
                    if i < len(perm) and perm[i] == num:
                        break
        return perms
