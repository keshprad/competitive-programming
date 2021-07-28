from typing import List
# Problem: https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            key = ''.join(sorted(word))
            anagrams[key] = anagrams.get(key, []) + [word]
        return list(anagrams.values())
