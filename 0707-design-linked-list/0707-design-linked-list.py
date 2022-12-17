class Node():
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        if self.head is None:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val
                    
    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        curr = self.head
        if curr is None:
            self.head = Node(val)
        else:
            while curr.next:
                curr = curr.next
            curr.next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            for i in range(index-1):
                curr = curr.next
            node = Node(val)
            node.next = curr.next
            curr.next = node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.size:
            curr = self.head
            if index == 0:
                self.head = curr.next
            else:
                for i in range(index-1):
                    curr = curr.next
                curr.next = curr.next.next
            self.size -= 1
