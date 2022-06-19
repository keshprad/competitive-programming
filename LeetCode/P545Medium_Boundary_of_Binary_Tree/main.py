from utils.tree import TreeNode
from typing import List
# Problem: https://leetcode.com/problems/boundary-of-binary-tree/


class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = [root.val]

        def left_boundary(node: TreeNode):
            # top down by appending before recursive call
            if node:
                # node is not root or a leaf node
                if node.left or node.right:
                    res.append(node.val)

                # traverse left boundary
                if node.left:
                    # left node if exists
                    left_boundary(node.left)
                elif node.right:
                    # right node if exists and left node does not
                    left_boundary(node.right)

        def right_boundary(node: TreeNode):
            # bottom up by appending after recursive call
            if node:
                # traverse right boundary
                if node.right:
                    # right node if exists
                    right_boundary(node.right)
                elif node.left:
                    # left node if exists and right node does not
                    right_boundary(node.left)

                # node is not root or a leaf node
                if node.left or node.right:
                    res.append(node.val)

        def leaves(node: TreeNode):
            if node:
                leaves(node.left)
                if node != root and node.left is None and node.right is None:
                    # node is not root and is a leaf (has no children)
                    res.append(node.val)
                leaves(node.right)

        left_boundary(root.left)
        leaves(root)
        right_boundary(root.right)
        return res
