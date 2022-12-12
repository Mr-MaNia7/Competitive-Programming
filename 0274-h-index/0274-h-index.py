class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 9, 7, 6, 2, 1        
        citations.sort(reverse=True)
        h_max = 0
        n = len(citations)
        for h, c in enumerate(citations):
            if c >= h+1:
                h_max = max(h+1, h_max)
        return h_max