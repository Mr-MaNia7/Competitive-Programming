from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opers = {'+', '*', '/', '-'}
        stack = []
        for c in tokens:
            if c in opers:
                y = stack.pop()
                x = stack.pop()
                print(x, y)
                if c == "+":
                    stack.append(int(x + y))
                if c == "-":
                    stack.append(int(x - y))
                if c == "*":
                    stack.append(int(x * y))
                if y != 0 and c == "/":
                    stack.append(int(x / y))                
            else:
                stack.append(int(c))
        return stack[0]
        
    
if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(["4","13","5","/","+"]))