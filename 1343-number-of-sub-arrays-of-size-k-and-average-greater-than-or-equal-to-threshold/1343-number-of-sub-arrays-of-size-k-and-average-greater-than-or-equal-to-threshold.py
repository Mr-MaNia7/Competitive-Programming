class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        l = 0
        r = k
        run_sum = sum(arr[0:k])
        if run_sum / k >= threshold:
                res += 1
        while r < len(arr):
            run_sum = run_sum + arr[r] - arr[l]
            if run_sum / k >= threshold:
                res += 1
            l += 1
            r += 1
        return res