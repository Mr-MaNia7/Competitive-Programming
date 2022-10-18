from itertools import accumulate
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefixSum = [1 if n & 1 else 0 for n in nums]
        for idx in range(len(nums)):
            prefixSum[idx] += prefixSum[idx-1] if idx-1 >= 0 else 0
        res = 0
        dic = {0: 1}
        for num in prefixSum:
            if num - k in dic:
                res += dic[num-k]
            dic[num] = dic.get(num, 0) + 1
        return res

if __name__ == "__main__":
    s = Solution()
    # print(s.numberOfSubarrays([1,2,1], 1))
    # print(s.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2,1,1,2,2], 2))
