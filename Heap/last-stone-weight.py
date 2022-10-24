import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            heav = heapq.nsmallest(2, maxheap)
            x = -heav[1]
            y = -heav[0]
            if x == y:
                heapq.heappop(maxheap)
                heapq.heappop(maxheap)
            else:
                heapq.heappop(maxheap)
                heapq.heapreplace(maxheap, -(y-x))
        return -maxheap[0] if maxheap else 0

if __name__ == "__main__":
    s = Solution()
    print(s.lastStoneWeight(stones = [2,2,2,2]))
