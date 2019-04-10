# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.vals = []
        self.inorder(root)
        min_diff = abs(self.vals[1] - self.vals[0])
        for i in range(2, len(self.vals)):
            min_diff = min(min_diff, abs(self.vals[i] - self.vals[i-1]))
        return min_diff
        
    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        self.vals.append(node.val)
        self.inorder(node.right)
            
