class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        dummyHead = ListNode()
        p = dummyHead
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1: 
            p.next = l1
        if l2:
            p.next = l2
        return dummyHead.next
