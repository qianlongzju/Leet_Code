from util import *
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        previous = head;
        q = 0
        while l1 and l2:
            p = q + l1.val + l2.val
            q = p / 10
            p %= 10
            a = ListNode(p)
            previous.next = a;
            previous = a;
            l1 = l1.next;
            l2 = l2.next;
        while l1:
            p = q + l1.val
            q = p / 10
            p %= 10
            a = ListNode(p)
            previous.next = a
            previous = a
            l1 = l1.next
        while l2:
            p = q + l2.val
            q = p / 10
            p %= 10
            a = ListNode(p)
            previous.next = a
            previous = a
            l2 = l2.next
        if q:
            a = ListNode(q)
            previous.next = a
        return head.next
