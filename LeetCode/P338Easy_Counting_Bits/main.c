// Problem: https://leetcode.com/problems/counting-bits/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *countBits(int n, int *returnSize) {
  *returnSize = n + 1;
  int *res = calloc(*returnSize, sizeof(int));

  for (int i = 0; i <= n; i++) {
    res[i] = res[i >> 1] + (i & 1);
  }

  return res;
}
