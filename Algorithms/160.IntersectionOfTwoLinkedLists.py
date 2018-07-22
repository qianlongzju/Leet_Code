class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lenA = self.getListLen(headA)
        lenB = self.getListLen(headB)
        if lenA > lenB:
            diff = lenA - lenB
            while diff:
                diff -= 1
                headA = headA.next
        else:
            diff = lenB - lenA
            while diff:
                diff -= 1
                headB = headB.next
        while headA and headB:
            if headA.val == headB.val:
                return headA
            headA = headA.next
            headB = headB.next


    def getListLen(self, headA):
        length = 0
        while headA:
            length += 1
            headA = headA.next
        return length
