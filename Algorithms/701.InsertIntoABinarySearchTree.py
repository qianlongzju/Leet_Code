# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        new_node = TreeNode(val)
        if root == None:
            return new_node
        node = root
        while node:
            if val > node.val:
                if node.right:
                    node = node.right
                else:
                    node.right = new_node
                    return root
            elif val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = new_node
                    return root
        return root
