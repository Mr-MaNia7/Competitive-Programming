from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        idx1 = 0
        idx2 = 1
        while idx2 < n:
            if nums[idx1] == 0 and nums[idx2] != 0:
                nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
                idx1 += 1
                idx2 += 1
            elif nums[idx1] == 0 and nums[idx2] == 0:
                idx2 += 1
            else:
                idx1 += 1
                idx2 += 1
            # print(idx1, idx2, nums)

if __name__ == "__main__":
    soln = Solution()
    soln.moveZeroes([0,1,0,3,12])