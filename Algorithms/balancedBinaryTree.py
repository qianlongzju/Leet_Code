class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.maxDepth(root) != -1

    def maxDepth(self, root):
        if not root: return 0
        left = self.maxDepth(root.left)
        if left == -1: return -1
        right = self.maxDepth(root.right)
        if right == -1: return -1

        return max(left, right) + 1 if abs(left - right) <= 1 else -1
