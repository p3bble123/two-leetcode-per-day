class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        myList = self.changeToList(head)
        return self.checkPalindrome(myList, 0)

    def changeToList(self, head):
        myList = []
        while head is not None:
            myList.append(head.val)
            head = head.next
        return myList

    def checkPalindrome(self, myList, curIdx):
        if curIdx > int(len(myList) / 2):
            # 중간에 도달 했으면 True
            return True
        if myList[curIdx] != myList[len(myList) - curIdx - 1]:
            return False
        else:
            return self.checkPalindrome(myList, curIdx + 1)
