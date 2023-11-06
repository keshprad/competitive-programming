from typing import List
# Problem: https://leetcode.com/problems/burst-balloons/


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}

        def maxCoins(l, r, lval, rval):
            '''
            l and r are the left and right indices of the subarray of nums currently looked at.
            lval and rval are the implicit values on the left and right of the array.
            '''
            if not nums:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            res = 0
            for i, num in enumerate(nums[l:r+1], start=l):
                # imagine if we popped num last:
                # (1) then we would use lval and rval to calculate the coins
                # (2) recurse on left partition... This means the new rval is
                # the balloon that would be popped last
                # (3) recurse on right partition... This means the new lval is
                # the balloon that would be popped last
                res = max(res, (lval*num*rval) +
                          maxCoins(l, i-1, lval, num) +
                          maxCoins(i+1, r, num, rval))
            dp[(l, r)] = res
            return dp[(l, r)]
        return maxCoins(0, len(nums)-1, 1, 1)
