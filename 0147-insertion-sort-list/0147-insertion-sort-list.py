class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted = None
        cur = head
        while cur:
            nxt = cur.next
            sorted = self.sortedInsert(sorted, cur)
            cur = nxt
        head = sorted
        return head
            
    def sortedInsert(self, head, new):
        if not head or head.val >= new.val:
            new.next = head
            head = new
        else:
            cur = head
            while cur.next and cur.next.val < new.val:
                cur = cur.next
            new.next = cur.next
            cur.next = new
        return head