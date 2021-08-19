from collections import defaultdict
from typing import List
# Problem: https://leetcode.com/problems/course-schedule-ii/


class Solution:
    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:
        # Early exit where no prereqs means any order is valid.
        if not prerequisites:
            return list(range(numCourses))

        # Mark all courses as unvisited
        visited = [0] * numCourses
        # Fill prereqs for courses
        graph = defaultdict(list)
        for course, source in prerequisites:
            graph[source].append(course)

        # Perform topilogical sort to find course order
        order = []
        for c in range(numCourses):
            if not self.top_sort_dfs(graph, visited, order, c):
                # If cycle exists, no order is possible. Return empty list
                return []

        return order[::-1]

    def top_sort_dfs(self, graph, visited, order, c):
        # 1 means node is visited
        # 0 means node is not visited
        # -1 means node is being visited. If we see -1 again, there is a loop

        if visited[c] == 1:
            return True
        elif visited[c] == -1:
            # There is a cycle. Cannot have a topological sort.
            return False
        else:
            visited[c] = -1
            for pre in graph[c]:
                if not self.top_sort_dfs(graph, visited, order, pre):
                    # There is a cycle. Cannot have a topological sort.
                    return False

            # Store order when a class with no prereqs is found.
            order.append(c)
            # Set course to visited
            visited[c] = 1
            return True
