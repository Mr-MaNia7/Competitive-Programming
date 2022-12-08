class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ng = []
        for i in nums1:
            found = False
            curr = float(inf)
            for j in nums2:
                if i == j: 
                    found = True
                    curr = j
                if found and j > curr:
                    ng.append(j)
                    break
            else:
                ng.append(-1)
        return ng