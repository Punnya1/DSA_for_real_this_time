from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    head = ListNode(arr[0])
    curr = head
    for i in arr[1:]:
        curr.next = ListNode(i)
        curr = curr.next
    return head

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        l,r = 0, len(arr) - 1
        while l < r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True

sol = Solution()
head = create_linked_list([1,2,2,1])
print(sol.isPalindrome(head))