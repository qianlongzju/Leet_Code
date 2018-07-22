class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        totalLength = self.genLength(head)
        if totalLength == 0 or totalLength == 1:
            return head
        leftLength = totalLength / 2
        leftHead = head
        rightHead = self.getRightHead(head, leftLength)
        leftHead = self.sortList(leftHead)
        rightHead = self.sortList(rightHead)
        return self.merge(leftHead, rightHead)
    
    def getRightHead(self, head, leftLength):
        rightHead = head
        i = 1
        while i < leftLength:
            rightHead = rightHead.next
            i += 1
        p = rightHead.next
        rightHead.next = None
        rightHead = p
        return rightHead
    
    def merge(self, leftHead, rightHead):
        headptr = ListNode(0)
        p = headptr
        while leftHead and rightHead:
            if leftHead.val < rightHead.val:
                p.next = leftHead
                leftHead = leftHead.next
            else:
                p.next = rightHead
                rightHead = rightHead.next
            p = p.next
        if leftHead:
            p.next = leftHead
        if rightHead:
            p.next = rightHead
        return headptr.next
        
    def genLength(self, head):
        p = head
        n = 0
        while p:
            n += 1
            p = p.next
        return n
