class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        for n in range(x+1):
            if  n*n > x:
                return res
            res = n
        return res