from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, prefixSum, d = 0, 0, {0:1}
        for num in nums:
            prefixSum += num
            if prefixSum-k in d:
                count += d[prefixSum-k]   
            if prefixSum in d:
                d[prefixSum] += 1
            else:
                d[prefixSum] = 1
        return count

if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([1,1,1], 2))