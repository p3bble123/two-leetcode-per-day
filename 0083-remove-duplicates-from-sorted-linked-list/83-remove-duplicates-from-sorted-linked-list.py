# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head

        curNode = head

        while curNode != None:
            nextNode = curNode.next
            while nextNode != None:
                if nextNode.val != curNode.val:
                    break
                nextNode = nextNode.next

            curNode.next = nextNode
            curNode = nextNode

        return head