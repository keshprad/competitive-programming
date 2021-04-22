# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not head.next:
            return None
        pos = 0

        behind = self
        curr = behind.next = head

        while curr:
            pos += 1
            if pos > n:
                behind = behind.next
            curr = curr.next

        behind.next = behind.next.next
        return self.next
