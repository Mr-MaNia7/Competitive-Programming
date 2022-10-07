from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = 0
        while sum(nums[pivot + 1:]) != sum(nums[:pivot]):
            if pivot == len(nums): 
                pivot = -1
                break
            pivot += 1
        return pivot if pivot < len(nums) else -1