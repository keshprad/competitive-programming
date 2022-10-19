from typing import Optional
# Problem: https://leetcode.com/problems/linked-list-cycle-ii/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()

        curr = head
        while curr:
            seen.add(curr)
            if curr.next in seen:
                return curr.next
            else:
                curr = curr.next
        return None
