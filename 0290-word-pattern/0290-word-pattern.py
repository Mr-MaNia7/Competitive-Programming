class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern): return False
        patdic = {}
        sdic = {}
        for i in range(len(pattern)):
            if pattern[i] in patdic:
                if s[i] != patdic[pattern[i]]:
                    return False
            elif s[i] in sdic:
                if pattern[i] != sdic[s[i]]:
                    return False
            else:
                patdic[pattern[i]] = s[i]
                sdic[s[i]] = pattern[i]
        return True