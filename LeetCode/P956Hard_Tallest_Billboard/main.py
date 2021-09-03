from typing import List
# Problem: https://leetcode.com/problems/tallest-billboard/


class Solution:
    # 2nd solution where I combined case 2.1 & 2.2
    # To avoid repetition, comments in tallestBillboard1() have a better/deeper explanation
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}

        # Try adding every rod to each currently tracked diff, overlap pair
        for rod in rods:
            for diff, y in dp.copy().items():
                # init state
                # |-------|--- diff ---|                tall side
                # |-- y --|                             low side

                # Case 1: Add rod to tall side
                dp[diff + rod] = max(dp.get(diff + rod, 0), y)

                # Case 2: Add rod to low side
                dp[abs(diff - rod)] = max(dp.get(abs(diff - rod), 0),
                                          y + min(diff, rod))
        return dp[0]

    def tallestBillboard1(self, rods: List[int]) -> int:
        # dict key is the diff between 2 steel supports (multiple rods welded together as 1)
        # dict value is the max overlap between the steel supports with a given diff
        dp = {0: 0}

        # Try adding every rod to each currently tracked diff, overlap pair
        for rod in rods:
            for diff, y in dp.copy().items():
                # init state
                # |-------|--- diff ---|                tall side
                # |-- y --|                             low side

                # Case 1: Add rod to tall side
                # |-------|--- diff ---|-- rod --|      tall side
                # |-- y --|                             low side
                dp[diff + rod] = max(dp.get(diff + rod, 0), y)

                # Case 2: Add rod to low side
                if diff >= rod:
                    # Case 2.1: Add rod to low side and diff >= rod
                    # |-------|--- diff ---|            tall side
                    # |-- y --|-- rod --|               low side
                    dp[diff - rod] = max(dp.get(diff - rod, 0), y + rod)
                else:
                    # Case 2.2: Add rod to low side and diff < rod
                    # |-------|--- diff ---|            tall side
                    # |-- y --|----- rod -----|         low side
                    dp[rod - diff] = max(dp.get(rod - diff, 0), y + diff)
        return dp[0]
