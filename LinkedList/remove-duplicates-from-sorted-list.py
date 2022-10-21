from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

if __name__ == "__main__":
    def printListNode(lst):
        while lst:
            print(lst.val, end=" ")
            lst = lst.next
    s = Solution()
    printListNode(s.deleteDuplicates(ListNode(2, ListNode(2, ListNode(2)))))