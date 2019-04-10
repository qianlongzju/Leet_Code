# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rightHead = slow.next
        slow.next = None
        leftHead = head
        leftHead = self.sortList(leftHead)
        rightHead = self.sortList(rightHead)
        return self.merge(leftHead, rightHead)

    def merge(self, leftHead, rightHead):
        dummyHead = ListNode(0)
        p = dummyHead
        while leftHead and rightHead:
            if leftHead.val < rightHead.val:
                p.next = leftHead
                leftHead = leftHead.next
            else:
                p.next = rightHead
                rightHead = rightHead.next
            p = p.next
        if leftHead:
            p.next = leftHead
        if rightHead:
            p.next = rightHead
        return dummyHead.next
