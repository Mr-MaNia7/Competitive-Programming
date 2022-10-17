from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def maxSum(first: int, second: int) -> int:
            anchor = ans = 0
            for idx in range(first + second, len(prefixSum)):
                anchor = max(anchor, prefixSum[idx - second] - prefixSum[idx - (first + second)])
                ans = max(ans, anchor + prefixSum[idx] - prefixSum[idx - second])
            return ans

        prefixSum = [0] * (len(nums) + 1)
        for idx, num in enumerate(nums):
            prefixSum[idx+1] = prefixSum[idx] + num
        print(prefixSum)
        return max(maxSum(firstLen, secondLen), maxSum(secondLen, firstLen))

if __name__ == "__main__":
    s = Solution()
    print(s.maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4], 1, 2))