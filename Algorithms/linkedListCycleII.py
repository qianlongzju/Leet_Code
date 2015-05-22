class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head: return None
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return fast
