from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        countPairs = 0
        for i in range(n):
          for j in range(i + 1, n):
            if nums[i] == nums[j]:
                countPairs += 1
        return countPairs

if __name__ == "__main__":
    s = Solution()
    res = s.numIdenticalPairs([1,1,1,1])
    print(res)