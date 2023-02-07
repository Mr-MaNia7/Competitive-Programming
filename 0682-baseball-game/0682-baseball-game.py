class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for p in operations:
            if p == 'C':
                stack.pop()
            elif p == 'D':
                stack.append(stack[-1]*2)
            elif p == '+':
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(p))
        return sum(stack)