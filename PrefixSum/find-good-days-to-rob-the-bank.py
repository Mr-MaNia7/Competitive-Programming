from typing import List

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        nonInc, nonDec = [0], [0]
        curr = 0
        for i in range(1, n):
            if security[i] <= security[i-1]: curr += 1
            else: curr = 0
            nonInc.append(curr)
        curr = 0
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i+1]: curr += 1
            else: curr = 0
            nonDec.append(curr)
        nonDec.reverse()
        return [i for i in range(n) if nonInc[i] >= time and nonDec[i] >= time]

if __name__ == "__main__":
    s = Solution()
    print(s.goodDaysToRobBank(security = [5,4,3,3,5,6,2], time = 2))
    # print(s.goodDaysToRobBank([1,2,5,4,1,0,2,4,5,3,1,2,4,3,2,4,8], time = 2))
