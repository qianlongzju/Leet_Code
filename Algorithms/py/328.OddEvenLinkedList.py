# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd_head, even_head = ListNode(0), ListNode(0)
        odd_p, even_p = odd_head, even_head
        node = head
        i = 1
        while node:
            if i % 2 == 1:
                odd_p.next = node
                odd_p = odd_p.next
            else:
                even_p.next = node
                even_p = even_p.next
            node = node.next
            i += 1
        even_p.next = None
        odd_p.next = even_head.next
        return odd_head.next
