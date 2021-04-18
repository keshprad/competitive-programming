from typing import List
# Problem: https://leetcode.com/problems/binary-tree-inorder-traversal/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root: TreeNode):
        return self.inorderHelper(root, [])

    def inorderHelper(self, root: TreeNode, res: List = []):
        if root:
            self.inorderHelper(root.left, res)
            res.append(root.val)
            self.inorderHelper(root.right, res)
        return res
