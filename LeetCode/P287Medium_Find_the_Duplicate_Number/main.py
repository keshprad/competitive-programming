from typing import List
# Problem: https://leetcode.com/problems/find-the-duplicate-number/


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # if we think of this as a linkedlist, the repeated number is the start of cycle
        # use floyd warshall algorithm for start of cycle

        # intersection of slow and fast
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # first intersection of the two slow pointers will be start of cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
