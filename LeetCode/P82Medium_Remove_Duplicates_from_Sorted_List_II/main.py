# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # use a sentinel node in case head is removed
        sent = prev = ListNode(None, head)

        while head:
            if head.next and head.val == head.next.val:
                # if duplicates exist, find last duplicate node
                while head.next and head.val == head.next.val:
                    head = head.next
                # set the predecessor to point to node after duplicates
                prev.next = head.next
            else:
                # move to next node
                prev = prev.next
            # move to next node
            head = head.next
        # return the head of new linkedlist
        return sent.next
