# Problem: https://leetcode.com/problems/palindrome-linked-list/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def isPalindrome(self, head: ListNode):
        # Base case
        if head is None or head.next is None:
            return True

        # Finds middle node
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse 2nd half of LinkedList
        new_next, curr = None, slow
        while curr:
            new_prev = curr.next
            curr.next = new_next
            new_next = curr
            curr = new_prev

        # Check is og list and reversed are equal
        curr = new_next
        while curr:
            if curr.val != head.val:
                return False
            head, curr = head.next, curr.next
        return True
