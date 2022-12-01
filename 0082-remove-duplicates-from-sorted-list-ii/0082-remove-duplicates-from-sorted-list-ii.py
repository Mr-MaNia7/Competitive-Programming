class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        write = dummy
        l = r = head
        while r:
            while r and l.val == r.val:
                r = r.next
            if l.next == r:
                write.next = l
                write = write.next
            l = r
        write.next = None
        return dummy.next