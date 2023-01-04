class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [1] * (n+1)
        ans = []
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] ^ arr[i-1]
        print(prefix)
        for q in queries:
            s = q[0]
            e = q[1]
            ans.append(prefix[e+1] ^ prefix[s])
        return ans