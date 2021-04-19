from typing import List
from collections import deque
# Problem: https://leetcode.com/problems/binary-tree-inorder-traversal/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, out = deque(), []

        while root is not None or stack:
            if root is not None:
                stack.append(root)
                root = root.left
            elif root is None and stack:
                root = stack.pop()
                out.append(root)
                root = root.right
        return out
