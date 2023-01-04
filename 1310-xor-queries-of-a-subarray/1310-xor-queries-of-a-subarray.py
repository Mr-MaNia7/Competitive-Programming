class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(len(arr)-1):
            arr[i+1] ^= arr[i]
        return [arr[e] ^ arr[s-1] if s else arr[e] for s, e in queries]