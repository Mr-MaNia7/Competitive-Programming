from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        prefix, suffix, n = 1, 1, len(nums)
        ans = [1] * n
        for idx in range(n):
            ans[idx] *= prefix
            ans[-idx-1] *= suffix
            prefix *= nums[idx]
            suffix *= nums[-idx-1]
        return ans
        
if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([2,3,4,5]))