from typing import Optional
# Problem: https://leetcode.com/problems/reverse-nodes-in-k-group/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None, None
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # returns head and tail of new list
        return prev, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sent = prevk = ListNode(-1, head)
        prev = sent
        curr = head

        while True:
            for i in range(k):
                if not curr:
                    return sent.next
                else:
                    prev = curr
                    curr = curr.next
            prev.next = None
            # reverse list
            revhead, revtail = self.reverse(prevk.next)

            prevk.next = revhead
            revtail.next = curr
            prevk = revtail
