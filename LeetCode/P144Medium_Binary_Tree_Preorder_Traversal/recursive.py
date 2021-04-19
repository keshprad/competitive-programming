from typing import List
# Problem: https://leetcode.com/problems/binary-tree-preorder-traversal/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursiveSolution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return self.preorder_traversal_helper(root, [])

    def preorder_traversal_helper(self, root: TreeNode, ans: List[int]):
        if root:
            ans.append(root.val)
            self.preorder_traversal_helper(root.left, ans)
            self.preorder_traversal_helper(root.right, ans)
        return ans
