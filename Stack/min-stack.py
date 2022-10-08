class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack: self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        if self.stack: self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1]

if __name__ == "__main__":
    obj = MinStack()
    print(obj.push(-2))
    print(obj.push(0))
    print(obj.push(-3))
    print(obj.stack)
    print(obj.getMin())
    print(obj.pop())
    print(obj.top())
    print(obj.getMin())