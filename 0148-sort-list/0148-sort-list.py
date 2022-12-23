class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        if not head.next: return head
        arr = []
        while head:
            arr.append((head.val, head))
            head = head.next
        arr.sort(key = lambda x: x[0])
        dummy = arr[0][1]
        for i in range(len(arr)-1):
            p = arr[i][1]
            p.next = arr[i+1][1]
        p.next = arr[-1][1]
        p = arr[-1][1]
        p.next = None
        return dummy
            