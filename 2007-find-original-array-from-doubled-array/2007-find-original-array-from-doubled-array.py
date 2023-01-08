class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        coll = collections.Counter(changed)
        if coll[0] % 2: return []
        for c in sorted(coll):
            if coll[c] > coll[c*2]:
                return []
            coll[c*2] -= coll[c] if c else coll[c] // 2
        return list(coll.elements())