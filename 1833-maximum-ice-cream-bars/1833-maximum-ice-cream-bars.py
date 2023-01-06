class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = summ = 0
        for c in costs:
            if summ + c > coins: break
            res += 1
            summ += c
        return res