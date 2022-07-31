from typing import Optional
# Problem: https://leetcode.com/problems/validate-binary-search-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if node:
                if left < node.val < right:
                    return valid(node.left, left, node.val) and valid(node.right, node.val, right)
                else:
                    return False
            else:
                return True
        return valid(root, -float('inf'), float('inf'))
