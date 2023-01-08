class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        maxm = 0
        for i, p in enumerate(points):
            x1, y1 = p[0], p[1]
            dic = {}
            for j in range(i+1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                if x2-x1:
                    m = (y2-y1)/(x2-x1)
                else:
                    m = float('inf')
                key = round(m, 10)
                if key in dic:
                    dic[key] += 1
                    maxm = max(dic[key], maxm)
                else:
                    dic[key] = 1
                    maxm = max(1, maxm)
        return maxm + 1