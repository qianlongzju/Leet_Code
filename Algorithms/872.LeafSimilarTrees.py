# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        result1, result2 = [], []
        self.preorder(root1, result1)
        self.preorder(root2, result2)
        return len(result1) == len(result2) and sum(abs(a-b) for a, b in zip(result1, result2)) == 0
        
    def preorder(self, root, result):
        if root == None:
            return
        if root.left == None and root.right == None:
            result.append(root.val)
        if root.left:
            self.preorder(root.left, result)
        if root.right:
            self.preorder(root.right, result)
        
