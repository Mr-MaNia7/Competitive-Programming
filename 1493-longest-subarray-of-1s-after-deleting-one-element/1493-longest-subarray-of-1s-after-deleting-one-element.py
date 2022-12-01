class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        zeroes = 0
        n = len(nums)
        l = r = 0
        while r < n:
            if zeroes < 2:
                if nums[r] == 0:
                    zeroes += 1
                r += 1
            else:
                if l < n and nums[l] == 0:
                    zeroes -= 1
                l += 1
            res = max(res, r - l - zeroes)
        return res - 1 if res == n else res