# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        val = root.val
        return self.check(root, val)
        
    def check(self, node, val):
        if node == None:
            return True
        if node.val != val:
            return False
        return self.check(node.left, val) and self.check(node.right, val)
