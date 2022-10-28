from typing import Optional
# Problem: https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False
            else:
                return t1.val == t2.val and is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)

        return is_mirror(root.left, root.right) if root else True
