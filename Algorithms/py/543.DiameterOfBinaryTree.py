# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        self.helper(root)
        return self.diameter
    
    def helper(self, node):
        if node == None:
            return 0
        left_path = self.helper(node.left)
        right_path = self.helper(node.right)
        self.diameter = max(self.diameter, left_path + right_path)
        return max(left_path, right_path) + 1
