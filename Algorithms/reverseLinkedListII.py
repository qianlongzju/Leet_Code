class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        headptr = ListNode(0)
        headptr.next = head
        ins, p = headptr, head
        for i in range(1, n):
            if i < m:
                ins, p = ins.next, p.next
            else:
                #p.next, p.next.next, ins.next =  p.next.next, ins.next, p.next
                temp = p.next
                p.next = temp.next
                temp.next = ins.next
                ins.next = temp
        return headptr.next
