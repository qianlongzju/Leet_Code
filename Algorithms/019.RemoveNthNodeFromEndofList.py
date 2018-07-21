class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
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
