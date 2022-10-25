from typing import List

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(num) for num in nums]
        nums.sort(reverse=True)
        return str(nums[k-1])

if __name__ == "__main__":
    s = Solution()
    print(s.kthLargestNumber(nums = ["3","6","7","10"], k = 4))