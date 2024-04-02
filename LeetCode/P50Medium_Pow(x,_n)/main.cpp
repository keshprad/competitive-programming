// Problem: https://leetcode.com/problems/powx-n/

class Solution {
public:
  double myPow(double x, int n) {
    if (x == 0 || x == 1) {
      // exit early
      return x;
    } else if (n == 0) {
      // exit early
      return 1;
    } else if (n == 1) {
      // exit early
      return x;
    } else if (n < 0) {
      // if n == INT_MIN, then -n results in integer overflow
      // -n = INT_MAX + 1
      // avoid integer overflow by removing one of the 1/x
      return 1 / x * myPow(1 / x, -(n + 1));
    } else if (n % 2 == 0) {
      double res = myPow(x, n / 2);
      return res * res;
    } else {
      return x * myPow(x, n - 1);
    }
  }
};