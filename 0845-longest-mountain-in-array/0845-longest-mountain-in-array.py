class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        c = 0
        l = 0
        n = len(arr)
        while l < n:
            r = l + 1
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
            l = max(r-1, l+1)
        return c