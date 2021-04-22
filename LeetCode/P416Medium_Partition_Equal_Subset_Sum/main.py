from typing import List
import numpy as np
# Problem: https://leetcode.com/problems/partition-equal-subset-sum/


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        total = total // 2

        bag = np.full(shape=total+1, fill_value=False)
        bag[0] = True

        for num in nums:
            for i in range(total, 0, -1):
                if i >= num and bag[i-num]:
                    bag[i] = True
        return bag[total]
