from collections import defaultdict, deque
from typing import List, Optional
# Problem: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = deque([(root, 0, 0)])
        traverse = defaultdict(lambda: defaultdict(list))
        min_x = max_x = 0
        max_y = 0

        while stack:
            root, curr_x, curr_y = stack.pop()
            if root:
                # Keep track of min and max x, so can easily able to return in order
                min_x, max_x = min(min_x, curr_x), max(max_x, curr_x)
                max_y = max(max_y, curr_y)
                #
                traverse[curr_x][curr_y].append(root.val)
                stack.append((root.right, curr_x+1, curr_y+1))
                stack.append((root.left, curr_x-1, curr_y+1))

        out = []
        for x in range(min_x, max_x+1):
            col = []
            for y in range(max_y+1):
                if traverse[x][y]:
                    col.extend(sorted(traverse[x][y]))
            out.append(col)
        return out
