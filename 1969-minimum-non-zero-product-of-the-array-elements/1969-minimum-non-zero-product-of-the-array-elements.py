class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        val = (2**p)-1
        x = val // 2
        mod = (10**9)+7
        return (pow(val-1, x, mod) * val) % mod