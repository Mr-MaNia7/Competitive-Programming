from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        prelist = []
        suflist = []
        ans = []
        for num in nums:
            prefix *= num
            prelist.append(prefix)
        for num in nums[::-1]:
            suffix *= num
            suflist.append(suffix)
        n = len(nums)
        for i in range(n):
            p = prelist[i-1] if i-1 >= 0 else 1
            s = suflist[n-1-(i+1)] if n-1-(i+1) >= 0 else 1
            ans.append(s * p)
        return ans 
        
if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([2,3,4,5]))