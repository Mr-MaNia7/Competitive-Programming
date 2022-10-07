from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)

if __name__ == "__main__":
    soln = Solution()
    soln.moveZeroes([0,0,1])