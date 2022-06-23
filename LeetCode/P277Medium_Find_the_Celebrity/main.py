# Problem: https://leetcode.com/problems/find-the-celebrity/

def knows(A: int, B: int) -> bool:
    # helper function that shows whether A knows B
    # this is not the actual logic of the func. LeetCode provides the `knows` helper function
    return True


class Solution:
    def findCelebrity(self, n: int) -> int:
        # find potential celeb
        celeb = 0
        for i in range(1, n):
            if not knows(i, celeb):
                celeb = i

        # validate
        for i in range(n):
            if not knows(i, celeb):
                # everyone should know the celeb
                return -1
            if celeb != i and knows(celeb, i):
                # celeb should not know anyone
                return -1

        return celeb
