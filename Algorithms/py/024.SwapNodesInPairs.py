class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy= ListNode(1)
        dummy.next = head
        prev, cur = dummy, head
        while cur and cur.next:
            q, r = cur.next, cur.next.next
            prev.next, q.next, cur.next = q, cur, r
            prev, cur = cur, r
        return dummy.next
