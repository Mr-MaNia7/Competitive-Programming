class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: x[1])
        res, end = 0, -float('inf')
        for p in points:
            if p[0] > end:
                res += 1
                end = p[1]
        return res