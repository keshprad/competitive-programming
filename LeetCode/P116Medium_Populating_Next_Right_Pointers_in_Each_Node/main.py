from typing import Optional
# Problem: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Definition for a Node.


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        head = curr = Node()
        parent = root

        while parent:
            for child in (parent.left, parent.right):
                curr.next = child
                if child:
                    curr = child

            if parent.next:
                parent = parent.next
            else:
                parent = head.next
                curr = head
        return root
