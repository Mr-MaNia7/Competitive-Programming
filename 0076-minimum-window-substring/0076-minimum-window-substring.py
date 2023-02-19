class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def equal(check, window):
            for k, v in check.items():
                if window.get(k, 0) < v:
                    return False
            return True
        tl, tr = -1, -1
        l = r = 0
        minm = float('inf')
        check = {}
        for c in t:
            check[c] = check.get(c, 0) + 1
        window = {}
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            while equal(check, window):
                if r-l+1 < minm:
                    minm = r-l+1
                    tl, tr = l, r
                window[s[l]] -= 1
                l += 1
        return '' if minm == float('inf') else s[tl:tr+1]