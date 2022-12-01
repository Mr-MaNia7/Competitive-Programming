class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = []
        k = k % len(nums)
        i = -k
        while i < len(nums) - k:
            l.append(nums[i])
            i += 1
        for i in range(len(nums)):
            nums[i] = l[i]