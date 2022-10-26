from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def checker(arr, s, e) -> bool:
            arr.sort()
            d = -1
            for i in range(s, e):
                if d == -1: d = arr[i-s+1] - arr[i-s]
                if arr[i-s+1] - arr[i-s] != d:
                    return False
            return True

        return [checker(nums[l[i]:r[i]+1], l[i], r[i]) for i in range(len(r))]

if __name__ == "__main__":
    s = Solution()
    print(s.checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]))