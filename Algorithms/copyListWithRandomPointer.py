class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        self.Clone(head)
        self.CopyRandomPointer(head)
        return self.restore(head)

    def Clone(self, head):
        while head:
            clonedNode = RandomListNode(head.label)
            clonedNode.next = head.next
            head.next = clonedNode
            head = clonedNode.next

    def CopyRandomPointer(self, head):
        while head:
            clonedNode = head.next
            if head.random:
                clonedNode.random = head.random.next
            head = clonedNode.next

    def restore(self, head):
        pClonedHead = RandomListNode(-1)
        pClonedNode = pClonedHead
        while head:
            pClonedNode.next = head.next
            pClonedNode = pClonedNode.next
            head.next = pClonedNode.next
            head = head.next
        return pClonedHead.next

