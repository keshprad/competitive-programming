// Problem:
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    unordered_map<char, int> map;

    int max_len = 0;
    int start = 0;
    for (int end = 0; end < s.length(); end++) {
      map[s[end]] = map.contains(s[end]) ? map[s[end]] + 1 : 1;

      while (map[s[end]] > 1) {
        map[s[start]] -= 1;
        start += 1;
      }

      max_len = std::max(max_len, end - start + 1);
    }

    return max_len;
  }
};