class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        left = 0
        stack = []
        for right in range(n):
            stack.append(pushed[right])
            while left < n and stack and stack[-1] == popped[left]:
                stack.pop()
                left += 1
        return False if stack else True