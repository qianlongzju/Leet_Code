# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.help(root)
        return root
        
    def help(self, node):
        if node == None:
            return True
        if self.help(node.left) == False:
            node.left = None
        if self.help(node.right) == False:
            node.right = None
        if node.left == None and node.right == None:
            return node.val == 1
        return True
