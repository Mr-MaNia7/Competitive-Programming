class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        res = 0
        for i in range(len(arr)):
            d = [0 for _ in range(101)]
            t = target - arr[i]
            for k in range(i + 1, len(arr)):
                if 0 <= t - arr[k] <= 100:
                    res += d[t-arr[k]]
                d[arr[k]]  += 1
        return res%(10**9+7)