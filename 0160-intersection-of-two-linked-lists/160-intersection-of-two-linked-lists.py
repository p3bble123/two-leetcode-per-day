# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)

        if lenA > lenB:
            curA = self.sendFast(headA, lenA - lenB)
            curB = headB
        elif lenB > lenA:
            curB = self.sendFast(headB, lenB - lenA)
            curA = headA
        else:
            curA = headA
            curB = headB

        while curA != None:
            if curA == curB:
                return curA

            curA = curA.next
            curB = curB.next

        return None

    def sendFast(self, head, nodes):
        cur = head
        while nodes > 0:
            cur = cur.next
            nodes -= 1

        return cur

    def getLength(self, head):
        cur = head
        curLength = 1

        while cur.next != None:
            curLength += 1
            cur = cur.next

        return curLength