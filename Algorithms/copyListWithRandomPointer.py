class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        self.Clone(head)
        self.CopyRandomPointer(head)
        return self.restore(head)

    def Clone(self, head):
        pNode = head
        while pNode:
            clonedNode = RandomListNode(pNode.label)
            clonedNode.next = pNode.next
            pNode.next = clonedNode
            pNode = clonedNode.next

    def CopyRandomPointer(self, head):
        pNode = head
        while pNode:
            clonedNode = pNode.next
            if pNode.random:
                clonedNode.random = pNode.random.next
            pNode = clonedNode.next

    def restore(self, head):
        pNode = head
        pClonedHead = None
        pClonedNode = None
        if pNode:
            pClonedHead = pNode.next
            pClonedNode = pNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next
        while pNode:
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next
        return pClonedHead

