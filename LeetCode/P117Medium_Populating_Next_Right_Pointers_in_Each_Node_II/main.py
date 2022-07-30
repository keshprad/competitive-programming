# Problem: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        '''O(n) time, O(1) space complexity'''
        # Idea is to iterate through each level of the tree like a linkedlist

        # dummy head node to start linkedlist
        head = curr = Node()
        parent = root

        while parent:
            # for each child, set the next
            for child in (parent.left, parent.right):
                curr.next = child
                if child:
                    # valid next node was set
                    curr = curr.next

            # parent having next indicates more nodes in level
            if parent.next:
                parent = parent.next
            else:
                # no more nodes in level
                # reset to next level.
                parent = head.next
                curr = head
        return root

    def connect1(self, root: 'Node') -> 'Node':
        '''O(n) time, O(n) space complexity'''
        if root:
            parent = [root]
            while parent:
                # find nodes in current level
                level = []
                for p in parent:
                    if p.left:
                        level.append(p.left)
                    if p.right:
                        level.append(p.right)

                # set next for current level
                for l in range(len(level)-1):
                    level[l].next = level[l+1]
                # curr level becomes new parent
                parent = level
        return root
