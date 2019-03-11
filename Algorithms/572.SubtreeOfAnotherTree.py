# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        self.result = False
        self.helper_1(s, t)
        return self.result
        
    def helper_1(self, s, t):
        if s.val == t.val and self.helper(s, t):
            self.result = True
            return
        if s.left:
            self.helper_1(s.left, t)
        if s.right:
            self.helper_1(s.right, t)
        
        
    def helper(self, s, t):
        if s == None or t == None:
            if s == None and t == None:
                return True
            else:
                return False
        if s.val != t.val:
            return False
        return self.helper(s.left, t.left) and self.helper(s.right, t.right)

        
