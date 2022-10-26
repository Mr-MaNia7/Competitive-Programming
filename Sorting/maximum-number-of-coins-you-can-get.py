import heapq
from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        return sum(piles[1:len(piles)-len(piles)//3:2])

if __name__ == "__main__":
    s = Solution()
    print(s.maxCoins(piles = [2,4,1,2,7,8]))