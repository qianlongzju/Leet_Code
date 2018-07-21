class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return head
        previous = head
        current = head.next
        while current:
            if current.val == previous.val:
                previous.next = current.next
                tmp = current
                current = current.next
                del tmp
            else:
                previous = previous.next
                current = current.next
        return head
