class Solution:
    def reverse(self, x):
        return x[::-1]
    def invert(self, x):
        r = ""
        for c in x:
            if c == "0": 
                r += "1"
            else: 
                r += "0"
        return r
    def findKthBit(self, n: int, k: int) -> str:
        s = ["0"] * 21
        for idx in range(2, n+1):
            s[idx] = s[idx-1] + "1" + self.reverse(self.invert(s[idx-1]))
        return s[n][k-1]