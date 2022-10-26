from typing import Counter, List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        map = {}
        count = 0
        for num in nums:
            res = k - num
            if res in map:
                count += 1
                if map.get(res) == 1: del map[res]
                else: map.update({res : map.get(res) - 1})
            else:
                map[num] = map.get(num, 0) + 1
        return count

if __name__ == "__main__":
    s = Solution()
    print(s.maxOperations(nums = [3,1,3,4,3], k = 6))