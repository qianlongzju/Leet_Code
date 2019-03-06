# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest_path = 0
        if root == None:
            return 0
        self.helper(root, root.val)
        return self.longest_path - 1
        
    def helper(self, node, val):
        if node == None:
            return 0
        left = self.helper(node.left, node.val)
        right = self.helper(node.right, node.val)
        self.longest_path = max(self.longest_path, left + right + 1)
        if node.val == val:
            return max(left, right) + 1
        return 0
