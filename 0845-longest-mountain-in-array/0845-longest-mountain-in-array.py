class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        c = 0
        r = 1
        l = 0
        n = len(arr)
        while r < n:
            isup = False
            isdown = False
            while r<n and arr[r] > arr[r-1]:
                r += 1
                isup = True
            while r<n and arr[r] < arr[r-1]:
                r += 1
                isdown = True
            if isup and isdown:
                c = max(c, r-l)
            if r<n and arr[r] == arr[r-1]:
                r += 1
            l = r - 1
        return c