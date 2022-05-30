// Problem: https://leetcode.com/problems/sum-of-two-integers/

int getSum(int a, int b) {
  int c = 1;

  while (c) {
    c = ((unsigned int)(a & b)) << 1;
    a ^= b;
    b = c;
  }
  return a;
}
