class Solution(object):
    def reverseList_iterative(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        current = head
        while current.next:
            p = current.next
            current.next = p.next
            p.next = dummyHead.next
            dummyHead.next = p
        return dummyHead.next
