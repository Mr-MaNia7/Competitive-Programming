class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for w in words:
            dic[w] = dic.get(w, 0) + 1
        res = sorted(dic, key = lambda x: (-dic[x], x))
        return res[:k]