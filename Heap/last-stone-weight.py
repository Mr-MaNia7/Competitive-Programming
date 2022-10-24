import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1 and maxheap[0] != 0:
            y = -heapq.heappop(maxheap)
            x = -heapq.heappop(maxheap)
            heapq.heappush(maxheap, -(y - x))
        return -maxheap[0] if maxheap else 0

if __name__ == "__main__":
    s = Solution()
    print(s.lastStoneWeight(stones = [2,2,2,2]))
