# http://jessicasco.github.io/blog/2015/05/22/python-swap-caution/
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
                #temp = p.next
                #p.next = temp.next
                #temp.next = ins.next
                #ins.next = temp

                #p.next, p.next.next, ins.next =  p.next.next, ins.next, p.next
                p.next.next, p.next,  ins.next =  ins.next, p.next.next, p.next
        return headptr.next

if __name__ == '__main__':
    S = Solution()
    #head = ListNode(3)
    #head.next = ListNode(5)
    head, head.next = ListNode(3), ListNode(5)
    S.reverseBetween(head, 1, 2)
