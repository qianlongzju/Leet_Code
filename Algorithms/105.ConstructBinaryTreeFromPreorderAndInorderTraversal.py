# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        return self.buildTreeHelper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)

    def buildTreeHelper(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
        if preStart > preEnd: return None
        root = TreeNode(preorder[preStart])
        if preStart == preEnd: return root
        for root_index in range(inStart, inEnd+1):
            if inorder[root_index] == root.val:
                break
        root.left = self.buildTreeHelper(preorder, preStart+1, preStart+root_index-inStart, inorder, inStart, root_index-1)
        root.right = self.buildTreeHelper(preorder, preStart+root_index-inStart+1, preEnd, inorder, root_index+1, inEnd)
        return root
