class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.max_path_sum = None
        self.findMax(root)
        return self.max_path_sum

    def findMax(self, root):
        if not root: return 0
        left = self.findMax(root.left)
        right = self.findMax(root.right)
        self.max_path_sum = max(self.max_path_sum, left + right + root.val)
        ret = root.val + max(left, right)
        return ret if ret > 0 else 0

