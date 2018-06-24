from leetcode import *
class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if k < 2 or not head:
            return head
        headptr = ListNode(0)
        headptr.next = head
        previous = headptr
        p = head
        pp = head
        count = 1
        while pp:
            if count == k:
                pp = pp.next
                while p.next != pp:
                    temp = p.next
                    p.next = temp.next
                    temp.next = previous.next
                    previous.next = temp
                previous = p
                p = p.next
                count = 1
            else:
                pp = pp.next
                count += 1
        return headptr.next
