from leetcode import *
class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummyHead = ListNode(1)
        dummyHead.next = head
        prev = dummyHead
        p = head
        while p and p.next:
            q = p.next
            r = p.next.next
            prev.next = q
            q.next = p
            p.next = r
            prev= p
            p = r
        return dummyHead.next
