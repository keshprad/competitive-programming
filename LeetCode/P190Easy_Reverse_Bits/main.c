// Problem: https://leetcode.com/problems/reverse-bits/

unsigned int reverseBits(unsigned int n) {
  unsigned int res = 0;
  if (n) {
    int i;
    for (i = 0; i < 32; i++) {
      res <<= 1;
      res += n & 1;
      n >>= 1;
    }
  }
  return res;
}