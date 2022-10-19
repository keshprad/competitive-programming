from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {None: None}

        # first populate dictionary with mapping from original node to copy
        curr = head
        while curr:
            copies[curr] = Node(curr.val)
            curr = curr.next

        # then set pointers for all copies to point to the copies of the pointers for original
        curr = head
        while curr:
            copies[curr].next = copies[curr.next]
            copies[curr].random = copies[curr.random]
            curr = curr.next

        # return copy of the head
        return copies[head]
