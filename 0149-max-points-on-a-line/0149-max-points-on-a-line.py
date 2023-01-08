class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        l = []
        maxm = 0
        # print(f'before {l}')
        for i, p in enumerate(points):
            x1, y1 = p[0], p[1]
            dic = {}
            for j in range(i+1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                if x2-x1:
                    m = (y2-y1)/(x2-x1)
                    # print(f"{(y2-y1)}/{(x2-x1)}")
                    b = y2 - m*x2
                else:
                    m = float('inf')
                    b = x1
                key = (round(m, 10), round(b, 10))
                if key in dic:
                    dic[key] += 1
                    maxm = max(dic[key], maxm)
                else:
                    dic[key] = 1
                    maxm = max(1, maxm)
            l.append(dic)
        # print(f'after {l}')
        return maxm + 1