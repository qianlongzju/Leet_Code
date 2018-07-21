class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return head
        headptr = ListNode(head.val-1)
        headptr.next = head
        previous = headptr
        p = head
        remove = False
        while p:
            while p and p.next and p.val == p.next.val:
                remove = True
                tmp = p
                p = p.next
                del tmp
            if remove:
                previous.next = p.next
                del p
                p = previous.next
                remove = False
            else:
                p = p.next
                previous = previous.next
        return headptr.next
