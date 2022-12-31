class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        for i in range(len(heights)-1):
            dce = heights[i+1] - heights[i]
            if dce > 0:
                heapq.heappush(pq, dce)
            if len(pq) > ladders:
                bricks -= heapq.heappop(pq)
            if bricks < 0:
                return i
        return len(heights)-1