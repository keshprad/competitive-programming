from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class IterativeSolution:
    # Solution #1
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, out = [(root, False)], []

        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    out.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return out

    # Solution #2
    def postorderTraversal_2(self, root: TreeNode) -> List[int]:
        stack, out = deque([root]), []

        while stack:
            root = stack.pop()
            if root:
                out.append(root.val)
                stack.append(root.left)
                stack.append(root.right)
        return out[::-1]
