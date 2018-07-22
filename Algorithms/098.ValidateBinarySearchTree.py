# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.validBST(root, None, None)

    def validBST(self, root, Min, Max):
        if not root:
            return True
        if Min != None and Min >= root.val:
            return False
        if Max != None and Max <= root.val:
            return False
        return (self.validBST(root.left, Min, root.val) 
            and self.validBST(root.right, root.val, Max))
