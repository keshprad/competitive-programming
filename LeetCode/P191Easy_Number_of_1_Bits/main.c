// Problem: https://leetcode.com/problems/number-of-1-bits/

int hammingWeight(unsigned int n) {
  int count = 0;
  while (n != 0) {
    n = n & (n - 1);
    count++;
  }
  return count;
}