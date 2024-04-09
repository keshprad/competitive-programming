from typing import Optional
# Problem: https://leetcode.com/problems/diameter-of-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        hcache = {}

        def height(root):
            if not root:
                return 0
            if root in hcache:
                return hcache[root]
            hcache[root] = 1 + max(height(root.left), height(root.right))
            return hcache[root]

        def diameter(root):
            if not root:
                return 0
            return max(diameter(root.left), diameter(root.right), 1 + height(root.left) + height(root.right))

        return diameter(root) - 1

    def diameterOfBinaryTree2(self, root: Optional[TreeNode]) -> int:
        def diameter(node, res):
            # Base case
            if not node:
                return 0

            # rec calc left and right diam
            left = diameter(node.left, res)
            right = diameter(node.right, res)

            # update max diameter found
            res[0] = max(res[0], left+right)

            return max(left, right) + 1

        res = [0]
        diameter(root, res)
        return res[0]
