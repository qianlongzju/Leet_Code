from util import *
class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head or not k:
            return head
        length = 1
        cur = head
        while cur.next:
            length += 1
            cur = cur.next
        k %= length
        k = length - k
        cur.next = head
        while k:
            cur = cur.next
            k -= 1
        head = cur.next
        cur.next = None
        return head
