from collections import deque
# Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Depth First Search
    def maxDepth_DFS(self, root: TreeNode) -> int:
        if root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        else:
            return 0

    # Breadth First Search
    def maxDepth_BFS(self, root: TreeNode) -> int:
        depth, level = 0, deque([root]) if root else deque()
        while level:
            depth += 1
            for i in range(len(level)):
                node = level.popleft()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
        return depth
