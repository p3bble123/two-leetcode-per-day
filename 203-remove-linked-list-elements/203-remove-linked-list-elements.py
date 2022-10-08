class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head is not None:
            # head가 None이 아닐동안, head.val이 val과 일치하면 head를 다음 노드로 이동
            if head.val == val:
                head = head.next
            else:
                break

        if head is None:
            # 바꾼 head가 None이면 head 반환
            return head

        else:
            # 바꾼 head가 None이 아니면 removeNode 호출
            self.removeNode(head, head.next, val)
            return head

    def removeNode(self, prev, cur, val):
        if cur is None:
            # 현재 노드가 None이면 탈출
            return

        if cur.val == val:
            prev.next = cur.next
            cur = cur.next
            self.removeNode(prev, cur, val)
        else:
            prev = cur
            cur = cur.next
            self.removeNode(prev, cur, val)
