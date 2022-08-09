from collections import defaultdict
# Problem: https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = defaultdict(int)

        for letter in s:
            dic[letter] += 1

        for letter in t:
            dic[letter] -= 1
            if dic[letter] < 0:
                return False

        for val in dic.values():
            if val != 0:
                return False
        return True
