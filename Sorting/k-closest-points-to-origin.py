from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        indices = {}
        for idx, pt in enumerate(points):
            x, y = pt[0], pt[1]
            dis = x**2 + y**2
            if not idx in indices:
                indices[idx] = dis
        return [points[idx] for idx, dis in sorted(indices.items(), key=lambda kv:(kv[1], kv[0]))[:k]]

if __name__ == "__main__":
    s = Solution()
    # print(s.kClosest([[0,1],[1,0]], 2))
    # print(s.kClosest([[2,2],[2,2],[2,2],[2,2],[2,2],[2,2],[1,1]], 1))