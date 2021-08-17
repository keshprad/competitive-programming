from typing import List
# Problem: https://leetcode.com/problems/course-schedule/


class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        # Mark all courses as unvisited
        visited = [0 for _ in range(numCourses)]
        # Fill prereqs for courses
        courses = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            courses[course].append(prereq)

        def courses_dfs(i):
            # 1 means node is visited
            # 0 means node is not visited
            # -1 means node is being visited. If we see -1 again, there is a loop
            if visited[i] == 1: return True
            if visited[i] == -1: return False

            visited[i] = -1
            for j in courses[i]:
                if not courses_dfs(j):
                    return False

            visited[i] = 1
            return True

        for i in range(numCourses):
            if not courses_dfs(i):
                # No way found to complete course
                return False
        return True
