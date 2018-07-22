class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head
        previous = dummyHead
        current = head
        while current:
            if current.val == val:
                previous.next = current.next
                current = current.next
            else:
                previous = previous.next
                current = current.next
        return dummyHead.next
