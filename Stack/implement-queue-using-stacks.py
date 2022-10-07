class MyQueue:
    def __init__(self) -> None:
        self.queue = []
        return None

    def push(self, x: int) -> None:
        self.queue.append(x)
        return None

    def pop(self) -> int:
        front = self.queue[0]
        self.queue = self.queue[1:]
        return front

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return True if len(self.queue) == 0 else False

if __name__ == "__main__":
    obj = MyQueue()
    # print(obj.push(1))
    # print(obj.push(2))
    # print(obj.queue)
    # print(obj.peek())
    # print(obj.pop())
    # print(obj.empty())