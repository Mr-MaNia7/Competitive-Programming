class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(n):
            if n == 2**i:
                return True
            elif 2**i > n:
                return False
        else:
            return False