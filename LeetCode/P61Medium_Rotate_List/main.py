# Problem: https://leetcode.com/problems/rotate-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        # Get len of list and last element
        last_node = head
        length = 1
        while last_node.next:
            last_node = last_node.next
            length += 1

        # If k > length, we just need to shift by remainder
        k %= length

        # Make linked list circular
        last_node.next = head

        # Iterate until getting to new last node
        for i in range(length - k):
            last_node = last_node.next

        # Break circular linked list and return new head
        new_head = last_node.next
        last_node.next = None
        return new_head
