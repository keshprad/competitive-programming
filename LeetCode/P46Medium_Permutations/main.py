from typing import List
# Problem: https://leetcode.com/problems/permutations/


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.permute_dfs(nums, [], permutations)
        return permutations

    # DFS helper for permute
    def permute_dfs(self, nums: List[int], path: List[int], permutations: List[List[int]]):
        if not nums:
            permutations.append(path)
        else:
            for i in range(len(nums)):
                self.permute_dfs(nums[:i]+nums[i+1:],
                                 path+[nums[i]], permutations)
