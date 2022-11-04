# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:   return list2
        if list2 == None:   return list1

        head = list1 if list1.val <= list2.val else list2

        while True:
            if list1 == None or list2 == None:
                return head

            if list1.val <= list2.val:
                while True:
                    if list1.next == None:  break
                    if list1.next.val > list2.val:  break
                    list1 = list1.next
                temp = list1.next
                list1.next = list2
                list1 = temp
            else:
                while True:
                    if list2.next == None:  break
                    if list2.next.val > list1.val:  break
                    list2 = list2.next
                temp = list2.next
                list2.next = list1
                list2 = temp
