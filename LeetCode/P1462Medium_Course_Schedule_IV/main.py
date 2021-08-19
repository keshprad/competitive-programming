from collections import defaultdict
from typing import List
# Problem: https://leetcode.com/problems/course-schedule-iv/


class Solution:
    # Use a modified Floyd-Warshall algorithm to find if all matrixes are connected.
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
