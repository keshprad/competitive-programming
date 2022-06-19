from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def construct_tree(tree: List[int]) -> TreeNode:
    if len(tree) == 0:
        return None
    else:
        nodes = [TreeNode(tree[0])]

    for i in range(1, len(tree)):
        node = TreeNode(tree[i]) if tree[i] is not None else None
        nodes.append(node)

        # index of parent node
        parent = int((i - 1) / 2)

        if (parent*2 + 1) == i:
            # left child
            nodes[parent].left = node
        else:
            # right child
            nodes[parent].right = node

    return nodes[0]
