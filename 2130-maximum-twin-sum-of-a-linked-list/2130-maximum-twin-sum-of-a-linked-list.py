# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        maxm = 0
        while prev and head:
            maxm = max(maxm, prev.val + head.val)
            prev = prev.next
            head = head.next
        return maxm