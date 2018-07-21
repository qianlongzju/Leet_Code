from leetcode import *
class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        leftheadptr = ListNode(0)
        rightheadptr = ListNode(0)
        left = leftheadptr
        right = rightheadptr
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        left.next = rightheadptr.next
        right.next = None
        return leftheadptr.next
