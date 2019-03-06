# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.helper(root)
        return self.sum
    
    def helper(self, node):
        if node == None:
            return
        if node.left != None and node.left.left == None and node.left.right == None:
            self.sum += node.left.val
        if node.left:
            self.helper(node.left)
        if node.right:
            self.helper(node.right)
