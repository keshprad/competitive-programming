from typing import List
# Problem: https://leetcode.com/problems/h-index/


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        npapers = len(citations)

        # h can be from [0, npapers]
        buckets = [0] * (npapers + 1)

        for num in citations:
            if num >= npapers:
                # we can treat a num citations > npapers the same since h <= npapers
                buckets[npapers] += 1
            else:
                buckets[num] += 1

        count = 0
        # go in reverse order to maximize h.
        for h in range(npapers, -1, -1):
            # at any point there are `count` papers with `h` or more citations.
            count += buckets[h]
            if count >= h:
                return h
        return 0
