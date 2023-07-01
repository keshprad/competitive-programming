from typing import List
import collections
import heapq
# Problem: https://leetcode.com/problems/task-scheduler/


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = collections.deque([])
        maxheap = []

        # fill max heap (priority is count of task)
        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1
        for task in counts:
            heapq.heappush(maxheap, (-counts[task], task))

        cycles = 0
        while counts:
            if maxheap:
                # get task from heap
                count, task = heapq.heappop(maxheap)

                # perform task
                count += 1      # add1 because count is negative

                # push to q for cooldown
                q.append((count, task))
                if not count:
                    del counts[task]
            else:
                # idle placeholder
                q.append(None)

            # check q is too long.
            if len(q) > n:
                pair = q.popleft()
                # task no longer idle.
                # push if not an idle placeholder.
                if pair and pair[0]:
                    heapq.heappush(maxheap, pair)

            # cycle done!!
            cycles += 1

        return cycles
