from typing import Optional
# Problem: https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(0, l1)

        carry = 0

        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = total // 10

            l1.val = total % 10

            prev = l1
            l1 = l1.next
            l2 = l2.next

        while l1:
            total = l1.val + carry
            carry = total // 10
            l1.val = total % 10

            prev = prev.next
            l1 = l1.next
            if carry == 0:
                l1 = None

        while l2:
            total = l2.val + carry
            carry = total // 10
            prev.next = ListNode(total % 10)

            prev = prev.next
            l2 = l2.next

        if carry:
            prev.next = ListNode(1)

        return dummy.next

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
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
