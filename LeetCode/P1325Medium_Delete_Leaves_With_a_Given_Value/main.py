from typing import Optional
# Problem: https://leetcode.com/problems/delete-leaves-with-a-given-value/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode],
                        target: int) -> Optional[TreeNode]:
        if root:
            # Postorder traversal to ensure children nodes are handled before parent node.
            # Left and Right are set to None if they are target leaves
            root.left = self.removeLeafNodes(root.left, target)
            root.right = self.removeLeafNodes(root.right, target)

            # If root is not a target leaf node, return root.
            if root.val != target or (root.left or root.right):
                return root

        # Returns None if no root or if root is a target leaf
        return None
