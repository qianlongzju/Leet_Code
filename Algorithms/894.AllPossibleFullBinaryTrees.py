# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N & 0x01 == 0:
            return []
        if N == 1:
            return [TreeNode(0)]
        result = []
        for left_size in range(1, N-1, 2):
            left_trees = self.allPossibleFBT(left_size)
            right_trees = self.allPossibleFBT(N-1-left_size)
            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(0)
                    root.left = left_tree
                    root.right = right_tree
                    result.append(root)
        return result
