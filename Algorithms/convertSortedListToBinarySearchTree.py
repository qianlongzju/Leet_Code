# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        self.listNode = head
        return self.sortedSubListToBST(0, n-1)

    def sortedSubListToBST(self, start, end):
        if start > end: return None
        mid = start + (end - start) / 2
        left = self.sortedSubListToBST(start, mid-1)
        parent = TreeNode(self.listNode.val)
        self.listNode = self.listNode.next
        parent.left = left
        parent.right = self.sortedSubListToBST(mid+1, end)
        return parent


