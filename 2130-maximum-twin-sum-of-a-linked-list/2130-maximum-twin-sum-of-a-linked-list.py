# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        l = 0
        r = len(arr)-1
        maxm = 0
        while l < r:
            maxm = max(maxm, arr[l].val + arr[r].val)
            r -= 1
            l += 1
        return maxm