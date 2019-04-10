class Solution:
    # @return a ListNode
    def removeNthFromEnd_old(self, head, n):
        index = 0
        p = head
        delete = None
        while p:
            p = p.next
            if delete:
                delete = delete.next
            index += 1
            if index == n+1:
                delete = head
        if index >= n+1:
            tmp = delete.next
            delete.next = delete.next.next
            del tmp
        else:
            tmp = head
            head = head.next
            del tmp
        return head

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head
        p, current = dummyHead, head
        for i in range(n):
            current = current.next
        while current:
            current = current.next
            p = p.next
        p.next = p.next.next
        return dummyHead.next
