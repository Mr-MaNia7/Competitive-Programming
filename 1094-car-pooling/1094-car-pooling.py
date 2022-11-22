class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lst = []
        for n, start, end in trips:
            lst.append((start, n))
            lst.append((end, -n))
        lst.sort()
        pas = 0
        for tup in lst:
            pas += tup[1]
            if pas > capacity:
                return False
        return True
