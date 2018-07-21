class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def reorderList(self, head):
        p = self.split(head)
        p = self.reverse(p)
        head = self.merge(head, p)
        return head

    def split(self, head):
        if not head:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        p = slow.next
        slow.next = None
        return p

    def reverse(self, head):
        headptr = ListNode(0)
        while head:
            tmp = head.next
            head.next = headptr.next
            headptr.next = head
            head = tmp
        return headptr.next

    def merge(self, p, q):
        head = ListNode(0)
        tmp = head
        while p and q:
            tmp.next = p
            p = p.next
            tmp = tmp.next
            tmp.next = q
            q = q.next
            tmp = tmp.next
        if p:
            tmp.next = p
        return head.next
