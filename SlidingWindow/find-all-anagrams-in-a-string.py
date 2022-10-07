from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        counter = Counter(p)
        idx1 = 0
        for idx2, c in enumerate(s):
            counter[c] -= 1
            while counter[c] < 0:
                counter[s[idx1]] += 1
                idx1 += 1
            if idx2 - idx1 + 1 == len(p):
                res.append(idx1)
        return res

if __name__ == "__main__":
    s = Solution()
    # print(s.findAnagrams("cbaebabacd", "abc"))
