# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left, right = root.left, root.right
        height = 0
        while right:
            left, right = left.left, right.right
            height += 1
        if left is None:
            return (1 << (height+1)) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
