#include <unordered_map>
// Problem: https://leetcode.com/problems/diameter-of-binary-tree/

// Definition for a binary tree node.
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
public:
  // soln 1
  std::unordered_map<TreeNode *, int> heights;

  int diameterOfBinaryTree(TreeNode *root) {
    if (!root)
      return 0;

    return std::max(height(root->left) + height(root->right) + 1,
                    std::max(diameterOfBinaryTree(root->left),
                             diameterOfBinaryTree(root->right))) -
           1;
  }

  int height(TreeNode *root) {
    if (!root)
      return 0;
    if (!heights.contains(root))
      heights[root] = 1 + std::max(height(root->left), height(root->right));

    return heights[root];
  }

  // soln 2
  int diameter(TreeNode *root, int res[]) {
    if (!root)
      return 0;

    int left = diameter(root->left, res);
    int right = diameter(root->right, res);

    res[0] = std::max(res[0], left + right);
    return std::max(left, right) + 1;
  }

  int diameterOfBinaryTree2(TreeNode *root) {
    int res[] = {0};
    diameter(root, res);
    return res[0];
  }
};