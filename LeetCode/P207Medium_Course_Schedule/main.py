from collections import defaultdict
from typing import List
# Problem: https://leetcode.com/problems/course-schedule/


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        # Mark all courses as unvisited
        visited = [0] * numCourses
        # Fill prereqs for courses
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        for i in range(numCourses):
            # Check if possible to take each course
            if not self.canTake(graph, visited, i):
                return False
        return True

    def canTake(self, graph, visited, i):
        # 1 means node is visited
        # 0 means node is not visited
        # -1 means node is being visited. If we see -1 again, there is a loop
        if visited[i] == 1: return True
        if visited[i] == -1: return False

        visited[i] = -1
        for j in graph[i]:
            if not self.canTake(graph, visited, j):
                return False

        visited[i] = 1
        return True
