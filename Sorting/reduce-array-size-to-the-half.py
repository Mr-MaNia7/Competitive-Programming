from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        n = len(arr) // 2
        for num in arr:
            d[num] = d.get(num, 0) + 1
        sum = 0
        count = 0
        for num in sorted(d.values(), reverse=True):
            if sum >= n:
                break
            sum += num
            count += 1
        return count

if __name__ == "__main__":
    s = Solution()
    print(s.minSetSize([1,9]))