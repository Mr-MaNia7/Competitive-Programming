from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        idx1 = 0
        idx2 = n - (k % n)
        while idx2 < n:
            nums.insert(idx1, nums.pop(idx2))
            idx1 += 1
            idx2 += 1
            # print(idx1, idx2, nums)

if __name__ == "__main__":
    soln = Solution()
    # soln.rotate([-1,-100,3,99], 2)
    soln.rotate([1, 2], 3)
