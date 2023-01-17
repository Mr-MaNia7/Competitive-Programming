class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        freq = 1
        i = summ = 0
        nums.sort()
        for j in range(len(nums)):
            summ += nums[j]
            while summ + k < nums[j] * (j - i + 1): # invalid condition
                summ -= nums[i]
                i += 1
            freq = max(freq, j - i + 1)
        return freq