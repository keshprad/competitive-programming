from collections import deque
from typing import List
# Problem: https://leetcode.com/problems/binary-tree-preorder-traversal/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack, out = deque([root]), []

        while stack:
            root = stack.pop()
            if root:
                out.append(root.val)
                stack.append(root.right)
                stack.append(root.left)
        return out
