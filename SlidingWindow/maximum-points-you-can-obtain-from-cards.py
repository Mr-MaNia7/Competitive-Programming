from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxPoint = 0
        for num in cardPoints[:k]:
            maxPoint += num
        currPoint = maxPoint
        for idx in range(k-1, -1, -1):
            currPoint += cardPoints[idx-k] - cardPoints[idx]
            maxPoint = max(maxPoint, currPoint)
        return maxPoint

if __name__ == "__main__":
    s = Solution()
    print(s.maxScore([1,2,3,4,5,6,1], 3))