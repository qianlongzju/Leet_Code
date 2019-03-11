# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        head = ListNode(0)
        carry = 0
        while s1 and s2:
            v1, v2 = s1.pop(), s2.pop()
            v = v1 + v2 + carry
            v, carry = v % 10, v / 10
            l = ListNode(v)
            l.next = head.next
            head.next = l
        while s1:
            v = s1.pop()
            v += carry
            v, carry = v % 10, v / 10
            l = ListNode(v)
            l.next = head.next
            head.next = l
        while s2:
            v = s2.pop()
            v += carry
            v, carry = v % 10, v / 10
            l = ListNode(v)
            l.next = head.next
            head.next = l
        if carry:
            l = ListNode(1)
            l.next = head.next
            head.next = l
        return head.next
