# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.vals = []
        self.helper(root)
        i, j = 0, len(self.vals) - 1
        while i < j:
            if self.vals[i] + self.vals[j] < k:
                i += 1
            elif self.vals[i] + self.vals[j] > k:
                j -= 1
            else:
                return True
        return False
    
    def helper(self, node):
        if node == None:
            return
        self.helper(node.left)
        self.vals.append(node.val)
        self.helper(node.right)
