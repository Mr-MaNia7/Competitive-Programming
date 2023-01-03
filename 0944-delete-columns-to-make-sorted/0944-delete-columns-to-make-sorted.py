class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        k = len(strs[0])
        n = len(strs)
        for i in range(k):
            run = ord(strs[0][i])
            for j in range(1, n):
                if run > ord(strs[j][i]):
                    res += 1
                    break
                else:
                    run = ord(strs[j][i])
        return res