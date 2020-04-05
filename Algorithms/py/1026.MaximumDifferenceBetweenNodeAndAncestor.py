# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, minimum, maximum):
            if node == None:
                return
            self.max_diff = max(self.max_diff, abs(maximum-node.val))
            self.max_diff = max(self.max_diff, abs(minimum-node.val))
            maximum = max(maximum, node.val)
            minimum = min(minimum, node.val)
            helper(node.left, minimum, maximum)
            helper(node.right, minimum, maximum)
        self.max_diff = 0
        helper(root, root.val, root.val)
        return self.max_diff
