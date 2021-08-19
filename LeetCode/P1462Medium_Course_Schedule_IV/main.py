from collections import defaultdict
from functools import lru_cache
from typing import List
# Problem: https://leetcode.com/problems/course-schedule-iv/


class Solution:
    # Solution using a modified Floyd-Warshall algorithm to find if all matrixes are connected.
    # Time: O(n^3)
    # Space: O(n^2)
    def checkIfPrerequisite(self, numCourses: int,
                            prerequisites: List[List[int]],
                            queries: List[List[int]]) -> List[bool]:
        # Set initial matrix to False everywhere (all nodes not connected)
        connected = [[False] * numCourses for _ in range(numCourses)]

        for pre, course in prerequisites:
            # Fill initial matrix with neighbor nodes
            # `pre` is connected to `course` (`pre` is a prerequisite for `course`)
            connected[pre][course] = True

        # For every pair of nodes, we check if another intermediary node could connect them.
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    # connected[i][j] is True if `i` is a direct prereq for `j`
                    # or if an intermediary prereq `k` exists between course `i` and course `j`
                    connected[i][j] = connected[i][j] or (connected[i][k]
                                                          and connected[k][j])
        return [connected[pre][course] for pre, course in queries]

    # Solution using DFS and lru_caching
    def checkIfPrerequisite2(self, numCourses: int,
                             prerequisites: List[List[int]],
                             queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for s, t in prerequisites:
            graph[s].append(t)

        @lru_cache(maxsize=None)
        def dfs(s, t):
            # Exit to prevent cycles
            if visited[s]:
                return False
            # Mark node as visited
            visited[s] = True

            # Nodes are connected! Return True
            if s == t:
                return True
            # Check neighbors
            return any(dfs(n, t) for n in graph[s])

        res = []
        for s, t in queries:
            visited = [False] * numCourses
            res.append(dfs(s, t))
        return res


sol = Solution()
print(
    sol.checkIfPrerequisite2(numCourses=2,
                             prerequisites=[[1, 0]],
                             queries=[[0, 1], [1, 0]]))
print(
    sol.checkIfPrerequisite2(numCourses=2,
                             prerequisites=[],
                             queries=[[1, 0], [0, 1]]))
print(
    sol.checkIfPrerequisite2(numCourses=3,
                             prerequisites=[[1, 2], [1, 0], [2, 0]],
                             queries=[[1, 0], [1, 2]]))
print(
    sol.checkIfPrerequisite2(numCourses=6,
                             prerequisites=[[1, 2], [1, 0], [2, 3], [3, 4],
                                            [4, 5], [5, 1]],
                             queries=[[2, 0]]))
