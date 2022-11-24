class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        run = 0
        l = 0
        count = float('inf')
        for r in range(len(nums)):
            run += nums[r]
            while run >= target:
                count = min(count, r - l + 1)
                run -= nums[l]
                l+=1
        return 0 if count == float(inf) else count
        
