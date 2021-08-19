import heapq
from typing import List
# Problem: https://leetcode.com/problems/course-schedule-iii/


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        if not courses:
            return 0

        pq, start_time = [], 0
        courses.sort(key=lambda course: course[1])
        for t, end_time in courses:
            start_time += t
            heapq.heappush(pq, -t)
            while start_time > end_time:
                start_time += heapq.heappop(pq)
        return len(pq)
