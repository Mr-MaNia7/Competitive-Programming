class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #O(n)
        map = {}
        for i, n in enumerate(nums):
            if n in map:
                return [i, map[n]]
            map[target-n] = i