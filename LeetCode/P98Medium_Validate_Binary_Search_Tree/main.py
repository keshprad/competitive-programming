from typing import Optional
from utils import TreeNode
# Problem: https://leetcode.com/problems/validate-binary-search-tree/


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if node:
                if left < node.val < right:
                    return True and valid(node.left, left, node.val) and valid(node.right, node.val, right)
                else:
                    return False
            else:
                return True
        return valid(root, -float('inf'), float('inf'))
