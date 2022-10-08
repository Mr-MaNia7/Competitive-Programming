from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for idx, num in enumerate(sorted(nums)):
            if num == target: arr.append(idx)
        return arr

if __name__ == "__main__":
    s = Solution()
    print(s.targetIndices([1,2,5,2,3], 6))