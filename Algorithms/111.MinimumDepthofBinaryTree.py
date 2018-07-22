class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not left: return 1 + right
        if not right: return 1 + left
        return 1 + min(left, right)
