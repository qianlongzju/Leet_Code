"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dummyHead = Node(0, None, None, None)
        dummyHead.next = head
        node = head
        prev = dummyHead
        q = []
        while node:
            if node.child:
                if node.next:
                    q.append(node.next)
                child = node.child
                node.next = child
                node.child = None
                child.prev = node
            elif node.next:
                node = node.next
            elif q:
                next_node = q.pop()
                node.next = next_node
                next_node.prev = node
                node = next_node
            else:
                node = node.next
        return dummyHead.next
