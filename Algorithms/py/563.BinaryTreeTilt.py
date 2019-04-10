# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[1]
        
    def helper(self, node):
        if node == None:
            return 0, 0
        left_sum, left_tilt = self.helper(node.left)
        right_sum, right_tilt = self.helper(node.right)
        return left_sum + right_sum + node.val, abs(left_sum - right_sum) + left_tilt + right_tilt
