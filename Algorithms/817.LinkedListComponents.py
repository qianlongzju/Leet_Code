# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        count = 0
        node = head
        flag = False
        while node:
            if node.val in G:
                flag = True
            else:
                if flag:
                    count += 1
                    flag = False
            node = node.next
        else:
            if flag:
                count += 1
        return count
