from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = {}
        for idx, num in enumerate(sorted(nums)):
            if num not in dic:
                dic[num] = idx
        return [dic[num] for num in nums]

if __name__ == "__main__":
    s = Solution()
    s.smallerNumbersThanCurrent([8,1,2,2,3])