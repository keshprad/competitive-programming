from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursiveSolution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return self.postorder_traversal_helper(root, [])

    def postorder_traversal_helper(self, root: TreeNode, out: List[int]) -> List[int]:
        if root:
            self.postorder_traversal_helper(root.left, out)
            self.postorder_traversal_helper(root.right, out)
            out.append(root.val)
        return out
