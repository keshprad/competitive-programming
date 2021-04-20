from collections import deque
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

    # Breadth First Search
    def minDepth_BFS(self, root: TreeNode) -> int:
        depth, level = 0, deque([root]) if root else deque()
        while level:
            depth += 1
            for i in range(len(level)):
                node = level.popleft()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                if not node.left and not node.right:
                    return depth
        return depth
