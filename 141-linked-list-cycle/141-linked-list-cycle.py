# Definition for singly-linked list.
# class ListNode:
#     def init(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        slow = head
        fast = head.next

        while True:
            if slow == fast:
                return True

            if fast == None or fast.next == None:
                return False

            slow = slow.next
            fast = fast.next.next