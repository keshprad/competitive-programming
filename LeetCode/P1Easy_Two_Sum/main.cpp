#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> seen;

    for (int i = 0; i < nums.size(); i++) {
      if (seen.contains(target - nums[i])) {
        return {i, seen[target - nums[i]]};
      }

      seen[nums[i]] = i;
    }

    return {};
  }
};
