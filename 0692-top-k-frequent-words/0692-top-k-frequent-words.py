class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for w in words:
            dic[w] = dic.get(w, 0) + 1
        heap = [(-v, k) for k, v in dic.items()]
        heapq.heapify(heap)
        res = []
        while k>0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res