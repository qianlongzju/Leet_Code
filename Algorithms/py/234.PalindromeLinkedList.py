# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        length = self.getListLength(head)
        if length % 2 == 0:
            step = length // 2
        else:
            step = (length - 1) // 2
        p = head
        step -= 1
        while step:
            p = p.next
            step -= 1
        if length % 2 == 1:
            l1 = p.next.next
            p.next = None
        else:
            l1 = p.next
            p.next = None
        l2 = self.reverseList(head)
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True

    def getListLength(self, head):
        n = 0
        while head:
            head = head.next
            n += 1
        return n

    def reverseList(self, head):
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
