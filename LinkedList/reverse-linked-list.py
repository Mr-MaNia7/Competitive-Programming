from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

if __name__ == "__main__":
    def printListNode(lst):
        while lst != None:
            print(lst.val, end=" ")
            lst = lst.next
    soln = Solution()
    printListNode(soln.reverseList(
        ListNode(2, ListNode(4, ListNode(3)))
        ))
