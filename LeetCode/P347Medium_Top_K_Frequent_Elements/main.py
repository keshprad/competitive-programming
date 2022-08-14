from typing import List
from collections import defaultdict
# Problem: https://leetcode.com/problems/top-k-frequent-elements/


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key is the num, val is count of the num
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        # Here, index is the count, value is an array of nums with that count
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            buckets[count].append(num)

        # get the k most occurring elements
        res = []
        i = -1
        while k > 0:
            res.extend(buckets[i])
            k -= len(buckets[i])
            i -= 1
        return res

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        return sorted(counts.keys(), key=lambda k: counts[k], reverse=True)[:k]
