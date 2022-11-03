from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        res = []
        for n in nums:
            map[n] = map.get(n, 0) + 1
        tgt = sorted(map.values(), reverse=True)[k-1]
        for key, val in map.items():
            if val >= tgt: res.append(key)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent(nums = [1,1,1,2,2,3], k = 2))