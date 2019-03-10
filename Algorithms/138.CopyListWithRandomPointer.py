"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        self.Clone(head)
        self.CopyRandomPointer(head)
        return self.restore(head)

    def Clone(self, head):
        while head:
            clonedNode = Node(head.val, None, None)
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
        pClonedHead = Node(-1, None, None)
        pClonedNode = pClonedHead
        while head:
            pClonedNode.next = head.next
            pClonedNode = pClonedNode.next
            head.next = pClonedNode.next
            head = head.next
        return pClonedHead.next
