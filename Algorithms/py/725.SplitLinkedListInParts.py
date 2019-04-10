# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        node = root
        length = 0
        while node:
            length += 1
            node = node.next
        a, b = length / k, length % k
        result = []
        start = root
        node = start
        bb = 1
        aa = 0
        while node:
            aa += 1
            if (bb <= b and aa == a + 1) or (bb > b and aa == a):
                result.append(start)
                start = node.next
                node.next = None
                node = start
                bb += 1
                aa = 0
            else:
                node = node.next
        while len(result) < k:
            result.append([])
        return result
