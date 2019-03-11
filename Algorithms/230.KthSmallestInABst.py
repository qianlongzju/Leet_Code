# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.index = 1
        self.helper(root, k)
        return self.result
    
    def helper(self, node, k):
        if node == None:
            return
        self.helper(node.left, k)
        if self.index > k:
            return 
        if self.index == k:
            self.result = node.val
            self.index += 1
            return
        self.index += 1
        self.helper(node.right, k)
