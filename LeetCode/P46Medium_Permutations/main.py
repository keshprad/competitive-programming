from typing import List
# Problem: https://leetcode.com/problems/permutations/


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.permute_dfs(nums, [], permutations)
        return permutations

    def permute_dfs(self, nums: List[int], path: List[int], permutations: List[List[int]]) -> List[List[int]]:
        if not nums:
            permutations.append(path)
        else:
            for i in range(len(nums)):
                self.permute_dfs(nums[:i]+nums[i+1:],
                                 path+[nums[i]], permutations)


sol = Solution()
print(sol.permute([1, 2, 3]))
print(sol.permute([0, 1]))
print(sol.permute([1]))
