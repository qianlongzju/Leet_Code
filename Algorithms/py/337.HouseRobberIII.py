# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.d = {}
        return self.try_rob(root)
    
    def try_rob(self, node):
        if node == None:
            return 0
        if node in self.d:
            return self.d[node]
        res1 = node.val
        if node.left:
            res1 += self.try_rob(node.left.left) + self.try_rob(node.left.right)
        if node.right:
            res1 += self.try_rob(node.right.left) + self.try_rob(node.right.right)
        res2 = self.try_rob(node.left) + self.try_rob(node.right)
        self.d[node] = max(res1, res2)
        return self.d[node]
