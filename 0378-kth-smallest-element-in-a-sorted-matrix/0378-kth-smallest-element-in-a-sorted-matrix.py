class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for row in matrix:
            for col in row:
                arr.append(col)
        arr.sort()
        return arr[k-1]