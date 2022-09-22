# Problem: https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(original: TreeNode, cloned: TreeNode, target):
            if original and cloned:
                if original == target:
                    return cloned
                else:
                    return dfs(original.left, cloned.left, target) or dfs(original.right, cloned.right, target)
            else:
                return None
        return dfs(original, cloned, target)
