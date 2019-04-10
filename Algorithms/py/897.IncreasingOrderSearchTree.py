# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        nodes = []
        self.increasingBSTHelper(root, nodes)
        if nodes:
            root = nodes[0]
            for i in range(1, len(nodes)):
                nodes[i-1].left, nodes[i-1].right = None, nodes[i]
            nodes[-1].left, nodes[-1].right = None, None
        return root
    
    def increasingBSTHelper(self, root, nodes):
        if root == None:
            return
        if root.left:
            self.increasingBSTHelper(root.left, nodes)
        nodes.append(root)
        if root.right:
            self.increasingBSTHelper(root.right, nodes)

