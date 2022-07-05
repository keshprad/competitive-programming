# Problem: https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        return self.say("1", n-1)

    def say(self, seq: str, n: int) -> str:
        if n == 0:
            return seq
        else:
            prev = seq[0]
            count = 1
            new_seq = ""
            for ch in seq[1:]:
                if ch == prev:
                    count += 1
                else:
                    new_seq += f'{count}{prev}'
                    prev = ch
                    count = 1
            new_seq += f'{count}{prev}'
            return self.say(new_seq, n-1)
