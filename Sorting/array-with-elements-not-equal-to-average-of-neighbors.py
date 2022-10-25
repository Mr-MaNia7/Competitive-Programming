from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums) // 2
        median = nums[n] if not n & 1 else (nums[n] + nums[n-1]) / 2
        ans = [0] * len(nums)
        odd = 1
        even = 0
        for n in nums:
            if n < median:
                ans[odd] = n
                odd += 2
            else:
                ans[even] = n
                even += 2
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.rearrangeArray(nums = [3,1,12,10,7,6,17,14,4,13]))