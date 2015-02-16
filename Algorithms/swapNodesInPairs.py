from leetcode import *
class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = prev.next
        nex = cur.next
        while nex:
            cur.next = nex.next
            nex.next = cur
            prev.next = nex
            
            prev = cur
            cur = cur.next
            if cur:
                nex = cur.next
            else:
                nex = None
        return dummy.next
