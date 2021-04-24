from typing import List
import collections


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = [0]*n
        fstack = collections.deque()

        for log in logs:
            log = log.split(':')
            log[0], log[2] = int(log[0]), int(log[2])

            if log[1] == 'start':
                # Append function starts
                fstack.append(log)
            elif log[1] == 'end':
                match = None
                timegap = 0

                # create a timegap for function calls within each other
                while not match or match[1] == 'gap':
                    match = fstack.pop()
                    if match[1] == 'gap':
                        timegap += match[2]

                # handles closing an open function
                # subtracts timegap to account for func calls within other functions
                if match[0] == log[0] and match[1] == 'start':
                    times[log[0]] += log[2] - match[2] + 1 - timegap
                    if fstack:
                        fstack.append([log[0], 'gap', log[2] - match[2] + 1])
        return times
