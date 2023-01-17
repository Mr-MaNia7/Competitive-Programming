class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l = 0
        r = 2
        res = 0
        while r < len(s):
            if not (s[l] == s[l+1] or s[l+1] == s[r] or s[l] == s[r]):
                res += 1
            l += 1
            r += 1
        return res