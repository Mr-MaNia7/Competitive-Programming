class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l = 0
        r = 3
        res = 0
        while r <= len(s):
            sett = set()
            for i in range(l, r):
                sett.add(s[i])
            if len(sett) == 3: res += 1
            l += 1
            r += 1
        return res