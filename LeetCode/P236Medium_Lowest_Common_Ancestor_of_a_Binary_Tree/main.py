# Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Found either p or q
        if root.val == p.val or root.val == q.val:
            return root
        # Look at the left and right subtrees
        leftNode = rightNode = None
        if root.left:
            leftNode = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            rightNode = self.lowestCommonAncestor(root.right, p, q)

        # At this point, we have found either p or q (or both) in the left or right subtree.
        if leftNode and rightNode:
            # Either p or q found in left tree and the other found in right subtree
            return root
        else:
            # p is found in the left or right subtree, or q is found in the left or right subtree
            # However, both are not found. If p is found in the left subtree, q would also be found at a lower level in the left subtree.
            # No need to search the rest of the subtree, just return
            return leftNode or rightNode
