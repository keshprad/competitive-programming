# Problem: https://leetcode.com/problems/minimum-depth-of-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Depth First Search
    def minDepth_DFS(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not root.right or not root.left:
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
