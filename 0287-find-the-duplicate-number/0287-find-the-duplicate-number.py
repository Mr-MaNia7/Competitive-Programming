class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        cur = nums[0]
        for n in nums[1:]:
            if n == cur:
                return n
            else:
                cur = n