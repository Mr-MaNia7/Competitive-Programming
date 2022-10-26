from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def checker(arr) -> bool:
            s = set(arr)
            if len(s) != len(arr): return len(s) == 1
            maxm, minm = max(arr), min(arr)
            if (maxm - minm)%(len(arr)-1) != 0: return False
            dce = (maxm - minm)//(len(arr)-1)
            for i in range(minm, maxm, dce):
                if i not in s:
                    return False
            return True

        return [checker(nums[start:stop+1]) for start, stop in zip(l,r)]

if __name__ == "__main__":
    s = Solution()
    print(s.checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]))