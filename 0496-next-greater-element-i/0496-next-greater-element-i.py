class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = {}
        monStack = [nums2[0]]
        for n in nums2:
            while monStack and n > monStack[-1]:
                hash[monStack.pop()] = n
            monStack.append(n)
        for n in monStack:
            hash[n] = -1
        res = []
        for n in nums1:
            res.append(hash[n])
        return res