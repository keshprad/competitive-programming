from collections import deque
# Problem: https://leetcode.com/problems/simplify-path/


class Solution(object):
    def simplifyPath(self, path: str):
        stack = deque()
        for directory in path.split("/"):
            if len(directory) == 0 or directory == ".":
                # Skip empty directories
                continue
            elif directory != "..":
                # Add valid directories
                stack.append(directory)
            elif stack:
                # Pop last in if directory is ".." and stack exists
                stack.pop()
        return "/" + "/".join(stack)
