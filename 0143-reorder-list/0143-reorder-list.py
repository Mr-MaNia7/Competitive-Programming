class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        while head:
            arr.append(head)
            head = head.next
        l = 0
        r = len(arr)-1
        while l < r:
            arr[l].next = arr[r]
            arr[r].next = arr[l+1]
            l += 1
            r -= 1
        arr[l].next = None