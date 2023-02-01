class Solution:
    def mergeTwoLists(self, h1: Optional[ListNode], h2: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative Two Pointers
        cur = dummy = ListNode()
        while h1 and h2:
            if h1.val <= h2.val:
                cur.next = h1
                h1, cur = h1.next, h1
            else:
                cur.next = h2
                h2, cur = h2.next, h2
        if h1 or h2:
            cur.next = h1 if h1 else h2
        return dummy.next