from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        for n in nums1:
            ge = -1
            for i in range(nums2.index(n)+1, len(nums2)):
                if nums2[i] > n:
                    ge = nums2[i]
                    break
            arr.append(ge)
        return arr

if __name__ == "__main__":
    s = Solution()
    print(s.nextGreaterElement([4,1,2], [1,3,4,2]))