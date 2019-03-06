# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return -1
        self.second_min = -1
        self.root_val = root.val
        self.helper(root)
        return self.second_min
        
    def helper(self, node):
        if node == None:
            return
        if node.val != self.root_val:
            if self.second_min == -1 or self.second_min > node.val: 
                self.second_min = node.val
        self.helper(node.left)
        self.helper(node.right)
