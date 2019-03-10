# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        left = [i for i in preorder[1:] if i < preorder[0]]
        right = [i for i in preorder[1:] if i > preorder[0]]

        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)
        return root
