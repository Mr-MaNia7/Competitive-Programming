class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        stk = []
        for i in range(len(nums)):
            while stk and int(nums[i]) < int(stk[-1]) and k:
                stk.pop()
                k -= 1
            stk.append(nums[i])
        res = ""
        begin = False
        for n in stk:
            if n != '0':
                begin = True
            if begin:
                res += n
        res = res[:-k] if k else res
        return "0" if res == "" else res
