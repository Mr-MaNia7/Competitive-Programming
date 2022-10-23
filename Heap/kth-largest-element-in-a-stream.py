import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pqueue = nums
        heapq.heapify(self.pqueue)
        while len(self.pqueue) > k:
            heapq.heappop(self.pqueue)
        print(self.pqueue)

    def add(self, val: int) -> int:        
        if len(self.pqueue) < self.k:
            heapq.heappush(self.pqueue, val)
        elif val > self.pqueue[0]:
            heapq.heapreplace(self.pqueue, val)
        return self.pqueue[0]

if __name__ == "__main__":
    kthLargest = KthLargest(3, [4,5,8,2])
    print(kthLargest.add(3))
    print(kthLargest.add(5))
    print(kthLargest.add(10))
    print(kthLargest.add(9))
    print(kthLargest.add(4))
    # kthLargest = KthLargest(2, [0])
    # print(kthLargest.add(-1))
    # print(kthLargest.add(1))
    # print(kthLargest.add(-2))
    # print(kthLargest.add(-4))
    # print(kthLargest.add(3))
