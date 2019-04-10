class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        current = dummyHead
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            digit = x + y + carry
            carry = digit / 10
            current.next = ListNode(digit % 10)
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry:
            current.next = ListNode(carry)
        return dummyHead.next
