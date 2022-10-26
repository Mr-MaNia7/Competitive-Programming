from typing import Counter, List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j, count = 0,len(nums) - 1, 0 
        while i < j:
            sum = nums[i] + nums[j]
            if sum == k:
                count += 1
                i += 1
                j -= 1
            elif sum > k:
                j -= 1
            else:
                i += 1
        return count

if __name__ == "__main__":
    s = Solution()
    print(s.maxOperations(nums = [3,1,3,4,3], k = 6))