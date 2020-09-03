# Problem: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.linked_list_to_int(head=l1)
        num2 = self.linked_list_to_int(head=l2)

        tot = str(num1 + num2)[::-1]
        head = self.int_to_linked_list(tot)

        return head

    def int_to_linked_list(self, n):
        head = None
        while len(n) != 0:
            digit = n[-1]
            head = ListNode(val=int(digit), next=head)
            n = n[:-1]
        return head

    def linked_list_to_int(self, head):
        num = ""
        while head is not None:
            num = str(head.val) + num
            head = head.next
        return int(num)