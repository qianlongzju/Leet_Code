# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        node = head
        l = 0
        while node:
            l += 1
            node = node.next
        result = [0] * l
        stack = []
        i = 0
        while head:
            while stack != [] and head.val > stack[-1][0]:
                node, index = stack.pop()
                result[index] = head.val
            stack.append((head.val, i))
            i += 1
            head = head.next
        return result
