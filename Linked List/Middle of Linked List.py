# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
#-----------------Pointer Based----------------#
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
#-----------------Array Based----------------#
        arr = []
        while head:
            arr.append(head)
            head = head.next
        if len(arr) % 2 == 0:
            return arr[(len(arr)//2)]
        return arr[len(arr)//2]
