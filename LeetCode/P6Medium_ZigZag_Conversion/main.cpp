#include <string>
// Problem: https://leetcode.com/problems/zigzag-conversion/

using namespace std;

class Solution {
public:
  string convert(string s, int numRows) {
    if (numRows == 1)
      return s;

    string res = "";
    int skip = 2 * (numRows - 1);

    for (int i = 0; i < numRows; i++) {
      int j = i;
      while (j < s.length()) {
        // process j
        res += s[j];

        // process j + skip - (2*i)
        // only process if i is not an edge
        if (0 < i && i < numRows - 1 && j + skip - (2 * i) < s.length())
          res += s[j + skip - (2 * i)];

        j += skip;
      }
    }
    return res;
  }
};