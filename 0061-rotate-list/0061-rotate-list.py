class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        d = head
        c = 0
        while d:
            c += 1
            d = d.next
        k %= c
        fast = slow = head
        for _ in range(k):
            fast = fast.next if fast.next else head
        while fast.next:
            slow = slow.next
            fast = fast.next
        node = slow
        while slow.next:
            slow = slow.next
        slow.next = head
        res = node.next
        node.next = None
        return res