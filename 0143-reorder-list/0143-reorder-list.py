class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        stack = []
        while slow and slow.next:
            stack.append(slow.next)
            slow = slow.next
        while head and stack:
            temp = head.next
            popp = stack.pop()
            head.next = popp
            popp.next = temp
            head = temp
        if head: head.next = None