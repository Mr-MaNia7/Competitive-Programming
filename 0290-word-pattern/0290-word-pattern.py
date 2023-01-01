class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern): return False
        pd = {}
        sd = {}
        for i in range(len(pattern)):
            if pattern[i] in pd:
                if s[i] != pd[pattern[i]]:
                    return False
            elif s[i] in sd:
                if pattern[i] != sd[s[i]]:
                    return False
            else:
                pd[pattern[i]] = s[i]
                sd[s[i]] = pattern[i]
        print(pd, sd)
        return True