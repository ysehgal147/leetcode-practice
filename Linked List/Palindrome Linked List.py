# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        current = head
        arr = []
        while current:
            arr.append(current.val)
            current = current.next
        if len(arr) == 0 or len(arr) == 1:
            return 1
        if arr == arr[::-1]:
            return 1
        return 0
