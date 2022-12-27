class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxm = 0
        sett = set()
        r = 0
        n = len(s)
        for l in range(n):
            while s[l] in sett:
                sett.remove(s[r])
                r += 1
            sett.add(s[l])
            maxm = max(maxm, l-r+1)
        return maxm