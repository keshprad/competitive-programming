# Problem: https://leetcode.com/problems/swap-nodes-in-pairs/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev, prev.next = self, head
        while prev.next and prev.next.next:
            node = prev.next
            nxt = node.next
            prev.next, node.next, nxt.next = nxt, nxt.next, node
            prev = node
        return self.next
