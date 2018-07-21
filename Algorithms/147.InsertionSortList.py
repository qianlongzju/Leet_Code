# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        previous, current = head, head.next;
        while current:
            if current.val >= previous.val:
                previous = previous.next
                current = current.next
                continue
            previous.next = current.next
            if head.val >= current.val:
                current.next = head
                head = current
            else:
                q, q_previous = head, None
                while q.val <= current.val:
                    q_previous = q
                    q = q.next
                current.next = q
                q_previous.next = current
            current = previous.next
        return head
