# Problem: https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contains(scount, tcount):
            for k in tcount:
                if scount[k] < tcount[k]:
                    return False
            return True

        if len(s) < len(t):
            return ''

        tcount, window = {}, {}
        for c in t:
            tcount[c] = tcount.get(c, 0) + 1

        have, need = 0, len(tcount)
        res, res_len = s, float('inf')

        l = 0
        r = 0
        while r < len(s):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in tcount and window[s[r]] == tcount[s[r]]:
                have += 1

            while have == need:
                # update res if optimal
                if (r - l + 1) < res_len:
                    res = s[l: r + 1]
                    res_len = r - l + 1

                # slide left pointer to decrease window
                window[s[l]] -= 1
                if s[l] in tcount and window[s[l]] < tcount[s[l]]:
                    have -= 1
                l += 1
            r += 1

        if res_len < float('inf'):
            return res
        else:
            return ''
