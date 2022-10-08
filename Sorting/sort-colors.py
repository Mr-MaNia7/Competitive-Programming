from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0] * 3
        for _, num in enumerate(nums):
          count[num] += 1
        for i in range(0, len(nums)):
            if i < count[0]:
                nums[i] = 0
            elif i < count[0] + count[1]:
                nums[i] = 1
            else:
                nums[i] = 2

if __name__ == "__main__":
    s = Solution()
    s.sortColors([2,0,2,1,1,0])