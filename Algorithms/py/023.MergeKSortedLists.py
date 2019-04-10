class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        def _mergeTwoLists(l1, l2):
            dummyHead = ListNode(1)
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

        if not lists:
            return None
        end = len(lists) -1 
        while end:
            begin = 0
            while begin < end:
                lists[begin] = _mergeTwoLists(lists[begin], lists[end])
                begin += 1
                end -= 1
        return lists[0]

