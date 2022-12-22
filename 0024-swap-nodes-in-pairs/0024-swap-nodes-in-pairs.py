class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        while curr and curr.next:
            prev.next = curr.next
            curr.next = prev.next.next
            prev.next.next = curr
            
            prev = curr
            curr = curr.next
        return dummy.next