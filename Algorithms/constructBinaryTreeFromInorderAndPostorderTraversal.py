# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        return self.buildTreeHelper(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)

    def buildTreeHelper(self, inorder, inStart, inEnd, postorder, postStart, postEnd):
        if inStart > inEnd: return None
        root = TreeNode(postorder[postEnd])
        if inStart == inEnd: return root
        for root_index in range(inStart, inEnd+1):
            if inorder[root_index] == root.val:
                break
        root.left = self.buildTreeHelper(inorder, inStart, root_index-1, 
                postorder, postStart, postStart+root_index-inStart-1)
        root.right = self.buildTreeHelper(inorder, root_index+1, inEnd,
                postorder, postStart+root_index-inStart, postEnd-1)
        return root

