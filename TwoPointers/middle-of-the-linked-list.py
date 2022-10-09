from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr != None:
            count += 1
            curr = curr.next
        c = head
        for i in range(count//2):
            c = c.next
        return c

if __name__ == "__main__":
    s = Solution()
    print(s.middleNode(head=ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))