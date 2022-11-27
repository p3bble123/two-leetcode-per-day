# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None

        fast, slow = head, head

        for i in range(n):
            fast = fast.next
            if fast == None:
                head = head.next
                return head

        while fast.next != None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head