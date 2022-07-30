from collections import defaultdict
from typing import List
# Problem: https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            # all anagrams will have the same key
            key = ''.join(sorted(word))
            anagrams[key].append(word)

        return list(anagrams.values())
