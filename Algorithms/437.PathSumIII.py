# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        self.helper_1(root, sum)
        return self.count
        
    def helper_1(self, node , sum):
        if node == None:
            return
        self.helper(node, sum)
        self.helper_1(node.left, sum)
        self.helper_1(node.right, sum)
        
    def helper(self, node, sum):
        if node == None:
            return
        sum -= node.val
        if sum == 0:
            self.count += 1
        self.helper(node.left, sum)
        self.helper(node.right, sum)
