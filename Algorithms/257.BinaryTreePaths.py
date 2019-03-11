# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.result = []
        if root:
            self.binaryTreePath(root, [])
        return self.result
            
    def binaryTreePath(self, root, path):
        path.append(str(root.val))
        if root.left:
            self.binaryTreePath(root.left, path[:])
        if root.right:
            self.binaryTreePath(root.right, path[:])
        if root.left == None and root.right == None:
            self.result.append("->".join(path))
            return
