from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        curr = head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        for i in range(len(lst)//2):
            if lst[i] != lst[-i-1]:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(ListNode(1, ListNode(1, ListNode(2)))))