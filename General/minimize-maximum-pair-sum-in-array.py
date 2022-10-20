from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxm = 0
        for idx in range(len(nums)//2):
            maxm = max(maxm, nums[idx] + nums[-idx-1])
        return maxm