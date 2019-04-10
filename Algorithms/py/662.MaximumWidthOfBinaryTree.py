# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        q = [(root, 1)]
        max_width = 0
        while q:
            size = len(q)
            max_width = max(max_width, q[-1][1]-q[0][1]+1)
            for i in range(size):
                node, idx = q.pop(0)
                if node.left:
                    q.append((node.left, 2*idx))
                if node.right:
                    q.append((node.right, 2*idx+1))
        return max_width
