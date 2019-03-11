# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.accum = 0
        self.helper(root)
        return root
        
    def helper(self, node):
        if node == None:
            return
        self.helper(node.right)
        node.val += self.accum
        self.accum = node.val
        self.helper(node.left)
